<template>
  <div class="transcript-analysis-view">
    <h2>Transcript Analysis</h2>
    <div class="input-area">
      <label for="transcript-input">Upload Transcript:</label>
      <input type="file" id="transcript-input" @change="handleFileUpload" accept=".txt,.text" />
    </div>
    <div class="options-area">
      <div class="format-selector">
        <label for="format-select">Output Format:</label>
        <select v-model="outputFormat" id="format-select">
          <option value="json">JSON</option>
          <option value="yaml">YAML</option>
          <option value="text">Text</option>
        </select>
      </div>
      <div class="button-area">
        <button @click="analyzeTranscript" :disabled="!file" class="analyze-btn">
          Analyze Transcript
        </button>
        <button 
          v-if="analysisResult" 
          @click="downloadResult" 
          class="download-btn"
        >
          Download Results
        </button>
      </div>
    </div>
    <div v-if="analysisResult" class="result-area">
      <h3>Analysis Results:</h3>
      <div class="result-grid">
        <div class="result-card">
          <h4>Word Frequencies</h4>
          <div class="word-freq">
            <div v-for="(count, word) in analysisResult.raw.word_counts" :key="word" class="word-item">
              <span class="word">{{ word }}</span>
              <span class="count">{{ count }}</span>
            </div>
          </div>
        </div>
        
        <div class="result-card">
          <h4>Quick Summary</h4>
          <p>{{ analysisResult.raw.quick_summary }}</p>
        </div>
        
        <div class="result-card">
          <h4>Sentiment Analysis</h4>
          <p>{{ analysisResult.raw.sentiment_analysis }}</p>
        </div>
        
        <div class="result-card">
          <h4>Keywords</h4>
          <div class="keywords">
            <span v-for="(keyword, index) in analysisResult.raw.keywords" 
                  :key="index" 
                  class="keyword-tag">
              {{ keyword }}
            </span>
          </div>
        </div>
        
        <div class="result-card full-width">
          <h4>Highlights</h4>
          <ul class="highlights-list">
            <li v-for="(point, index) in analysisResult.raw.bullet_point_highlights" 
                :key="index">
              {{ point }}
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div v-if="error" class="error-area">
      <p>Error: {{ error }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      file: null,
      analysisResult: null,
      error: null,
      outputFormat: 'json'
    };
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    async analyzeTranscript() {
      this.analysisResult = null;
      this.error = null;
      if (!this.file) {
        this.error = 'Please upload a transcript file.';
        return;
      }
      try {
        const formData = new FormData();
        formData.append('transcript', this.file);
        formData.append('output_format', this.outputFormat);
        
        const response = await axios.post('http://localhost:8000/analyze-transcript', formData);
        console.log('Response:', response); // Debug log
        
        if (response && response.data) {
          this.analysisResult = response.data;
          console.log('Analysis Result:', this.analysisResult); // Debug log
        } else {
          console.error('No data in response'); // Debug log
          throw new Error('No data received from server');
        }
      } catch (err) {
        this.error = err.message || 'Failed to analyze transcript.';
      }
    },
    async downloadResult() {
      if (!this.analysisResult) return;
      
      let content = '';
      let filename = `analysis-result.${this.outputFormat}`;
      let type = 'text/plain';
      
      // Create form data for the download request
      const formData = new FormData();
      formData.append('transcript', this.file);
      formData.append('output_format', this.outputFormat);
      
      try {
        // Get formatted version for download
        const formatResponse = await axios.post('http://localhost:8000/analyze-transcript', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          responseType: this.outputFormat === 'json' ? 'json' : 'text'
        });
        
        if (this.outputFormat === 'json') {
          content = JSON.stringify(formatResponse.data, null, 2);
          type = 'application/json';
        } else if (this.outputFormat === 'yaml') {
          content = formatResponse.data.formatted;
          type = 'application/x-yaml';
        } else {
          content = formatResponse.data;
          type = 'text/plain';
        }
        
        const blob = new Blob([content], { type });
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
      } catch (err) {
        this.error = err.message || 'Failed to download analysis result.';
      }
    }
  }
};
</script>

<style scoped>
.transcript-analysis-view {
  padding: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.input-area {
  margin-bottom: 20px;
}

.input-area label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.options-area {
  display: flex;
  gap: 20px;
  align-items: center;
  margin-bottom: 20px;
}

.format-selector {
  display: flex;
  gap: 10px;
  align-items: center;
}

.format-selector select {
  padding: 5px;
  border-radius: 4px;
  border: 1px solid #ddd;
}

.button-area {
  display: flex;
  gap: 10px;
}

.analyze-btn, .download-btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.analyze-btn {
  background-color: #4CAF50;
  color: white;
}

.analyze-btn:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.download-btn {
  background-color: #2196F3;
  color: white;
}

.result-area {
  margin-top: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 20px;
  background-color: #f9f9f9;
}

.error-area {
  color: #f44336;
  margin-top: 10px;
  padding: 10px;
  border-radius: 4px;
  background-color: #ffebee;
}

.result-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 20px;
}

.result-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.result-card h4 {
  margin-top: 0;
  color: #2196F3;
  border-bottom: 2px solid #e0e0e0;
  padding-bottom: 10px;
  margin-bottom: 15px;
}

.full-width {
  grid-column: 1 / -1;
}

.word-freq {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.word-item {
  background: #e3f2fd;
  padding: 5px 10px;
  border-radius: 15px;
  display: flex;
  gap: 8px;
  align-items: center;
}

.word {
  font-weight: bold;
}

.count {
  background: #2196F3;
  color: white;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 0.9em;
}

.keywords {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.keyword-tag {
  background: #e8f5e9;
  color: #2e7d32;
  padding: 5px 12px;
  border-radius: 15px;
  font-size: 0.9em;
}

.highlights-list {
  list-style-type: none;
  padding: 0;
}

.highlights-list li {
  padding: 10px;
  background: #fafafa;
  margin-bottom: 8px;
  border-radius: 4px;
  border-left: 4px solid #2196F3;
}
</style>
