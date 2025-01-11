<template>
  <div class="layout-wrapper" :class="{ 'dark-theme': isDarkTheme }">
    <Menubar class="header" :model="menuItems">
      <template #start>
        <div class="logo">
          <i class="pi pi-server mr-2"></i>
          AI-Ecosystem
        </div>
      </template>
      <template #end>
        <Button 
          :icon="isDarkTheme ? 'pi pi-sun' : 'pi pi-moon'" 
          class="p-button-rounded p-button-text mr-2"
          @click="toggleTheme" 
          v-tooltip.bottom="isDarkTheme ? 'Switch to Light Mode' : 'Switch to Dark Mode'"
        />
        <Button icon="pi pi-user" class="p-button-rounded p-button-text" />
      </template>
    </Menubar>
    
    <main class="main-content">
      <router-view />
    </main>

    <footer class="footer">
      <p>&copy; 2025 AI-Ecosystem. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
import Menubar from 'primevue/menubar';
import Button from 'primevue/button';
import Tooltip from 'primevue/tooltip';

export default {
  components: {
    Menubar,
    Button
  },
  directives: {
    tooltip: Tooltip
  },
  data() {
    return {
      isDarkTheme: false,
      menuItems: [
        {
          label: 'Home',
          icon: 'pi pi-home',
          to: '/'
        },
        {
          label: 'Dashboard',
          icon: 'pi pi-chart-line',
          to: '/dashboard'
        },
        {
          label: 'Releases',
          icon: 'pi pi-tag',
          to: '/releases'
        },
        {
          label: 'About',
          icon: 'pi pi-info-circle',
          to: '/about'
        }
      ]
    }
  },
  methods: {
    toggleTheme() {
      this.isDarkTheme = !this.isDarkTheme;
      if (this.isDarkTheme) {
        document.documentElement.setAttribute('data-theme', 'dark');
      } else {
        document.documentElement.setAttribute('data-theme', 'light');
      }
    }
  },
  mounted() {
    // Check system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      this.isDarkTheme = true;
      document.documentElement.setAttribute('data-theme', 'dark');
    }
  }
}
</script>

<style lang="scss">
.layout-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.header {
  background: #1a1a1a;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;

  .logo {
    font-size: 1.5rem;
    font-weight: bold;
  }

  .nav-menu {
    display: flex;
    gap: 1.5rem;

    .nav-link {
      color: white;
      text-decoration: none;
      padding: 0.5rem 1rem;
      border-radius: 4px;
      transition: background-color 0.3s;

      &:hover {
        background-color: rgba(255, 255, 255, 0.1);
      }

      &.router-link-active {
        background-color: #42b983;
      }
    }
  }
}

.main-content {
  flex: 1;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.footer {
  background: #f5f5f5;
  padding: 1rem;
  text-align: center;
  margin-top: auto;
}

body {
  margin: 0;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
    Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

* {
  box-sizing: border-box;
}
</style>
