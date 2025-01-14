<template>
  <div class="dashboard">
    <div class="grid">
      <div class="col-12">
        <Card>
          <template #title>
            <div class="flex align-items-center">
              <i class="pi pi-server mr-2"></i>
              AI System Status
            </div>
          </template>
          <template #content>
            <div class="grid">
              <div class="col-12 md:col-3">
                <Card class="status-card">
                  <template #title>Active Models</template>
                  <template #content>
                    <div class="text-3xl text-primary">12</div>
                    <Tag severity="success" value="Running" />
                  </template>
                </Card>
              </div>
              <div class="col-12 md:col-3">
                <Card class="status-card">
                  <template #title>API Requests</template>
                  <template #content>
                    <div class="text-3xl text-primary">2.4k</div>
                    <Tag severity="info" value="Today" />
                  </template>
                </Card>
              </div>
              <div class="col-12 md:col-3">
                <Card class="status-card">
                  <template #title>System Load</template>
                  <template #content>
                    <div class="text-3xl text-primary">65%</div>
                    <Tag severity="warning" value="Moderate" />
                  </template>
                </Card>
              </div>
              <div class="col-12 md:col-3">
                <Card class="status-card">
                  <template #title>Uptime</template>
                  <template #content>
                    <div class="text-3xl text-primary">99.9%</div>
                    <Tag severity="success" value="Stable" />
                  </template>
                </Card>
              </div>
            </div>
          </template>
        </Card>
      </div>

      <div class="col-12 md:col-6">
        <Card>
          <template #title>
            <div class="flex align-items-center">
              <i class="pi pi-cog mr-2"></i>
              Active AI Models
            </div>
          </template>
          <template #content>
            <Timeline :value="modelEvents" class="custom-timeline">
              <template #content="slotProps">
                <div class="flex align-items-center">
                  <i :class="slotProps.item.icon"></i>
                  <div class="ml-2">
                    <span class="font-bold">{{ slotProps.item.name }}</span>
                    <p class="text-sm text-gray-600">{{ slotProps.item.status }}</p>
                  </div>
                </div>
              </template>
            </Timeline>
          </template>
        </Card>
      </div>

      <div class="col-12 md:col-6">
        <Card>
          <template #title>
            <div class="flex align-items-center">
              <i class="pi pi-bolt mr-2"></i>
              Quick Actions
            </div>
          </template>
          <template #content>
            <div class="grid">
              <div class="col-6">
                <Button label="Deploy Model" icon="pi pi-upload" class="p-button-lg w-full mb-2" />
              </div>
              <div class="col-6">
                <Button label="Monitor" icon="pi pi-chart-line" class="p-button-lg w-full mb-2" severity="secondary" />
              </div>
              <div class="col-6">
                <Button label="Settings" icon="pi pi-cog" class="p-button-lg w-full mb-2" severity="help" />
              </div>
              <div class="col-6">
                <Button label="Reports" icon="pi pi-file" class="p-button-lg w-full mb-2" severity="info" />
              </div>
            </div>
          </template>
        </Card>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      modelEvents: [
        { name: 'Text Generation Model', status: 'Running - 99% uptime', icon: 'pi pi-check text-green-500' },
        { name: 'Image Recognition', status: 'Processing queue: 23 items', icon: 'pi pi-sync text-blue-500' },
        { name: 'Speech Analysis', status: 'Idle - Ready for requests', icon: 'pi pi-clock text-gray-500' },
        { name: '3D Environment Sim', status: 'Training in progress', icon: 'pi pi-spin pi-spinner text-orange-500' }
      ]
    }
  }
}
</script>

<style scoped>
.dashboard {
  padding: 1rem;
}

.status-card {
  text-align: center;
}

.custom-timeline ::v-deep(.p-timeline-event-content) {
  padding: 0.5rem;
}

.custom-timeline ::v-deep(.p-timeline-event-separator) {
  width: 2px;
  background-color: var(--primary-color);
}

.text-primary {
  color: var(--primary-color);
}
</style>
