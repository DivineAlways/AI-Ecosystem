<template>
  <div class="home">
    <Card class="welcome-card">
      <template #header>
        <img alt="AI Banner" src="@/assets/ai-banner.jpg" />
      </template>
      <template #title>
        <h1 class="text-4xl font-bold mb-2">Welcome to AI Ecosystem</h1>
      </template>
      <template #content>
        <p class="text-xl mb-4">Your comprehensive platform for AI model management, 3D environments, and intelligent automation</p>
        
        <div class="grid">
          <div class="col-12 md:col-3">
            <Card class="feature-card">
              <template #header>
                <i class="pi pi-cog text-4xl text-primary"></i>
              </template>
              <template #title>Model Management</template>
              <template #content>
                <p>Deploy and manage AI models with enterprise-grade controls</p>
                <Tag value="HIPAA Compliant" severity="success" class="mt-2" />
              </template>
            </Card>
          </div>
          
          <div class="col-12 md:col-3">
            <Card class="feature-card">
              <template #header>
                <i class="pi pi-cube text-4xl text-primary"></i>
              </template>
              <template #title>3D Environments</template>
              <template #content>
                <p>Create and simulate 3D environments for training and testing</p>
                <Tag value="Omniverse Ready" severity="info" class="mt-2" />
              </template>
            </Card>
          </div>
          
          <div class="col-12 md:col-3">
            <Card class="feature-card">
              <template #header>
                <i class="pi pi-users text-4xl text-primary"></i>
              </template>
              <template #title>Agent Systems</template>
              <template #content>
                <p>Deploy intelligent agents for automated decision making</p>
                <Tag value="Multi-Agent" severity="warning" class="mt-2" />
              </template>
            </Card>
          </div>
          
          <div class="col-12 md:col-3">
            <Card class="feature-card">
              <template #header>
                <i class="pi pi-shield text-4xl text-primary"></i>
              </template>
              <template #title>Enterprise Security</template>
              <template #content>
                <p>Built-in security features for business compliance</p>
                <Tag value="Government Ready" severity="danger" class="mt-2" />
              </template>
            </Card>
          </div>
        </div>

        <div class="mt-4">
          <Card>
            <template #title>
              <div class="flex align-items-center">
                <i class="pi pi-check-circle mr-2"></i>
                Getting Started
              </div>
            </template>
            <template #content>
              <div class="grid">
                <div class="col-12 md:col-4">
                  <Button 
                    label="Launch Dashboard" 
                    icon="pi pi-arrow-right" 
                    class="p-button-lg w-full"
                    @click="$router.push('/dashboard')" 
                  />
                </div>
                <div class="col-12 md:col-4">
                  <Button 
                    label="View Documentation" 
                    icon="pi pi-book" 
                    class="p-button-lg w-full p-button-secondary"
                    @click="$router.push('/docs')" 
                  />
                </div>
                <div class="col-12 md:col-4">
                  <Button 
                    label="Watch Tutorial" 
                    icon="pi pi-video" 
                    class="p-button-lg w-full p-button-help"
                    @click="$router.push('/tutorial')" 
                  />
                </div>
                <div class="col-12 md:col-4">
                  <Button
                    label="Analyze Transcript"
                    icon="pi pi-file-edit"
                    class="p-button-lg w-full p-button-success"
                    @click="$router.push('/transcript-analysis')"
                  />
                </div>
              </div>
            </template>
          </Card>
        </div>
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
