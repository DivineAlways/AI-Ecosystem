<template>
  <div class="documentation-page">
    <Card>
      <template #title>Documentation</template>
      <template #content>
        <div class="documentation-content">
          <h2>AI-Ecosystem Platform Documentation</h2>
          
          <div class="doc-section">
            <h3>Overview</h3>
            <p>The AI-Ecosystem Platform is a comprehensive solution for AI model management, 
               transcript analysis, and automated code improvements.</p>
          </div>

          <div class="doc-section">
            <h3>Core Features</h3>
            <div class="feature-list">
              <h4>Transcript Analysis</h4>
              <ul>
                <li>Upload and process text transcripts</li>
                <li>Generate word frequency analysis</li>
                <li>Create visualizations</li>
                <li>Export results in multiple formats</li>
              </ul>

              <h4>AI Director</h4>
              <ul>
                <li>Automated code analysis</li>
                <li>Smart refactoring suggestions</li>
                <li>Code quality improvements</li>
                <li>Performance optimization</li>
              </ul>

              <h4>Dashboard</h4>
              <ul>
                <li>Real-time metrics</li>
                <li>Project analytics</li>
                <li>Custom reporting</li>
              </ul>
            </div>
          </div>

          <div class="doc-section">
            <h3>API Reference</h3>
            <p>For detailed API documentation, please refer to our API Reference Guide.</p>
          </div>

          <div class="doc-section">
            <h3>Additional Resources</h3>
            <ul>
              <li><router-link to="/tutorial">Getting Started Tutorial</router-link></li>
              <li><router-link to="/releases">Release History</router-link></li>
              <li><a href="#">API Reference</a></li>
              <li><a href="#">Developer Guide</a></li>
            </ul>
          </div>
        </div>
      </template>
    </Card>
  </div>
</template>

<script>
import Card from 'primevue/card';

export default {
  name: 'Documentation',
  components: {
    Card
  }
}
</script>

<style scoped>
.documentation-page {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.documentation-content {
  line-height: 1.6;
}

.doc-section {
  margin: 2rem 0;
}

.doc-section h3 {
  color: var(--primary-color);
  margin-bottom: 1rem;
  border-bottom: 2px solid var(--surface-border);
  padding-bottom: 0.5rem;
}

.doc-section h4 {
  color: var(--text-color);
  margin: 1rem 0;
}

.feature-list ul {
  list-style-type: none;
  padding-left: 1.5rem;
  margin-bottom: 1.5rem;
}

.feature-list li {
  margin: 0.5rem 0;
  position: relative;
}

.feature-list li:before {
  content: "•";
  color: var(--primary-color);
  position: absolute;
  left: -1.5rem;
}

.doc-section a {
  color: var(--primary-color);
  text-decoration: none;
}

.doc-section a:hover {
  text-decoration: underline;
}
</style>
