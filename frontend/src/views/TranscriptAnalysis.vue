<template>
  <div class="transcript-analysis-view">
    <h2>Transcript Analysis</h2>
    <div class="input-area">
      <label for="transcript-input">Upload Transcript:</label>
      <input type="file" id="transcript-input" @change="handleFileUpload" accept=".txt,.text" />
    </div>
    <div class="button-area">
      <button @click="analyzeTranscript" :disabled="!file">Analyze Transcript</button>
    </div>
    <div v-if="analysisResult" class="result-area">
      <h3>Analysis Results:</h3>
      <div v-if="analysisResult.quick_summary">
        <h4>Quick Summary:</h4>
        <p>{{ analysisResult.quick_summary }}</p>
      </div>
      <div v-if="analysisResult.bullet_point_highlights && analysisResult.bullet_point_highlights.length">
        <h4>Bullet Point Highlights:</h4>
        <ul>
          <li v-for="(point, index) in analysisResult.bullet_point_highlights" :key="index">{{ point }}</li>
        </ul>
      </div>
      <div v-if="analysisResult.sentiment_analysis">
        <h4>Sentiment Analysis:</h4>
        <p>{{ analysisResult.sentiment_analysis }}</p>
      </div>
      <div v-if="analysisResult.keywords && analysisResult.keywords.length">
        <h4>Keywords:</h4>
        <ul>
          <li v-for="(keyword, index) in analysisResult.keywords" :key="index">{{ keyword }}</li>
        </ul>
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
      error: null
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
        const response = await axios.post('http://localhost:8000/analyze-transcript', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        this.analysisResult = response.data;
      } catch (err) {
        this.error = err.message || 'Failed to analyze transcript.';
      }
    }
  }
};
</script>

<style scoped>
.transcript-analysis-view {
  padding: 20px;
}

.input-area {
  margin-bottom: 20px;
}

.input-area label {
  display: block;
  margin-bottom: 5px;
}

.button-area {
  margin-bottom: 20px;
}

.result-area {
  margin-top: 20px;
  border: 1px solid #ddd;
  padding: 10px;
}

.error-area {
  color: red;
  margin-top: 10px;
}
</style>
