<router-view />
<template>
  <div class="tutorial-page">
    <Card>
      <template #title>Getting Started Tutorial</template>
      <template #content>
        <div class="tutorial-content">
          <h2>Welcome to AI-Ecosystem</h2>
          
          <div class="tutorial-section">
            <h3>1. Transcript Analysis</h3>
            <p>Upload and analyze text transcripts:</p>
            <ul>
              <li>Navigate to the Transcript Analysis page</li>
              <li>Upload a .txt file containing your transcript</li>
              <li>Choose visualization options (bar, pie, or line charts)</li>
              <li>Get AI-powered insights and word frequency analysis</li>
            </ul>
          </div>

          <div class="tutorial-section">
            <h3>2. AI Director</h3>
            <p>Use our automated code improvement system:</p>
            <ul>
              <li>Configure your improvement goals</li>
              <li>Let the AI analyze and enhance your code</li>
              <li>Review suggested changes and improvements</li>
              <li>Apply verified enhancements automatically</li>
            </ul>
          </div>

          <div class="tutorial-section">
            <h3>3. Dashboard</h3>
            <p>Monitor your project metrics:</p>
            <ul>
              <li>View analysis history</li>
              <li>Track code improvements</li>
              <li>Export reports and visualizations</li>
            </ul>
          </div>
        </div>
      </template>
    </Card>
  </div>
</template>

<script>
export default {
  name: 'Tutorial'
}
</script>

<style scoped>
.tutorial-page {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.tutorial-content {
  line-height: 1.6;
}

.tutorial-section {
  margin: 2rem 0;
}

.tutorial-section h3 {
  color: var(--primary-color);
  margin-bottom: 1rem;
}

.tutorial-section ul {
  list-style-type: none;
  padding-left: 1.5rem;
}

.tutorial-section li {
  margin: 0.5rem 0;
  position: relative;
}

.tutorial-section li:before {
  content: "•";
  color: var(--primary-color);
  position: absolute;
  left: -1.5rem;
}
</style>
