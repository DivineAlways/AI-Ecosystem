<template>
  <div class="home">
    <Card class="welcome-card">
      <template #header>
        <img alt="AI Banner" src="@/assets/ai-banner.jpg" />
      </template>
      <template #title>
        Welcome to AI Ecosystem
      </template>
      <template #content>
        <p class="text-xl mb-4">Your intelligent solution for AI management and deployment</p>
        <div class="grid">
          <div class="col-12 md:col-4">
            <Card class="feature-card">
              <template #header>
                <i class="pi pi-cog text-4xl text-primary"></i>
              </template>
              <template #title>Easy Management</template>
              <template #content>
                Manage your AI models with intuitive controls
              </template>
            </Card>
          </div>
          <div class="col-12 md:col-4">
            <Card class="feature-card">
              <template #header>
                <i class="pi pi-bolt text-4xl text-primary"></i>
              </template>
              <template #title>Fast Deployment</template>
              <template #content>
                Deploy models to production in minutes
              </template>
            </Card>
          </div>
          <div class="col-12 md:col-4">
            <Card class="feature-card">
              <template #header>
                <i class="pi pi-chart-bar text-4xl text-primary"></i>
              </template>
              <template #title>Real-time Analytics</template>
              <template #content>
                Monitor performance and usage metrics
              </template>
            </Card>
          </div>
        </div>
      </template>
      <template #footer>
        <Button label="Get Started" icon="pi pi-arrow-right" class="p-button-lg" @click="$router.push('/dashboard')" />
      </template>
    </Card>
  </div>
</template>

<script>
import Card from 'primevue/card';
import Button from 'primevue/button';

export default {
  name: 'Home',
  components: {
    Card,
    Button
  }
}
</script>

<style scoped>
.home {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.welcome-card {
  margin-bottom: 2rem;
}

.welcome-card :deep(img) {
  width: 100%;
  height: 300px;
  object-fit: cover;
}

.feature-card {
  text-align: center;
  height: 100%;
}

.feature-card :deep(.p-card-header) {
  padding-top: 2rem;
}

.text-primary {
  color: var(--primary-color);
}
</style>
