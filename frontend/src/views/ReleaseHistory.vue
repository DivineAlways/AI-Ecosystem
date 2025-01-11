<template>
  <div class="releases">
    <Card>
      <template #title>
        Release History
      </template>
      <template #content>
        <Timeline :value="releases" class="release-timeline">
          <template #content="slotProps">
            <Card class="mb-3">
              <template #title>
                <span class="text-xl">{{ slotProps.item.version }}</span>
                <Tag :severity="slotProps.item.severity" class="ml-2">
                  {{ slotProps.item.type }}
                </Tag>
              </template>
              <template #subtitle>
                {{ slotProps.item.date }}
              </template>
              <template #content>
                <ul class="list-none p-0 m-0">
                  <li v-for="(change, index) in slotProps.item.changes" 
                      :key="index"
                      class="mb-2">
                    <i :class="getChangeIcon(change.type)" class="mr-2"></i>
                    {{ change.description }}
                  </li>
                </ul>
              </template>
            </Card>
          </template>
        </Timeline>
      </template>
    </Card>
  </div>
</template>

<script>
import Timeline from 'primevue/timeline';
import Card from 'primevue/card';
import Tag from 'primevue/tag';

export default {
  name: 'ReleaseHistory',
  components: {
    Timeline,
    Card,
    Tag
  },
  data() {
    return {
      releases: [
        {
          version: 'v1.2.0',
          date: 'January 11, 2025',
          type: 'Feature',
          severity: 'success',
          changes: [
            { type: 'feature', description: 'Added dark theme support' },
            { type: 'feature', description: 'Introduced release history page' },
            { type: 'enhancement', description: 'Improved UI responsiveness' }
          ]
        },
        {
          version: 'v1.1.0',
          date: 'January 10, 2025',
          type: 'Enhancement',
          severity: 'info',
          changes: [
            { type: 'enhancement', description: 'Enhanced dashboard analytics' },
            { type: 'fix', description: 'Fixed navigation menu responsiveness' }
          ]
        },
        {
          version: 'v1.0.0',
          date: 'January 1, 2025',
          type: 'Major',
          severity: 'warning',
          changes: [
            { type: 'feature', description: 'Initial release' },
            { type: 'feature', description: 'Basic dashboard functionality' },
            { type: 'feature', description: 'User authentication' }
          ]
        }
      ]
    }
  },
  methods: {
    getChangeIcon(type) {
      const icons = {
        feature: 'pi pi-star text-green-500',
        enhancement: 'pi pi-arrow-up text-blue-500',
        fix: 'pi pi-check text-orange-500'
      }
      return icons[type] || 'pi pi-info'
    }
  }
}
</script>

<style lang="scss" scoped>
.releases {
  max-width: 800px;
  margin: 0 auto;
}

.release-timeline {
  .p-timeline-event-content {
    width: 100%;
  }
}

:deep(.p-card) {
  margin-bottom: 1rem;
}

.dark-theme {
  :deep(.p-card) {
    background-color: var(--surface-card);
    color: var(--text-color);
  }
}
</style>
