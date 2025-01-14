<template>
  <div class="layout-wrapper" :class="{ 'dark-theme': isDarkTheme }">
    <Menubar class="header" :model="menuItems">
      <template #start>
        <router-link to="/" class="logo">
          <i class="pi pi-cube mr-2"></i>
          AI-Ecosystem Platform
        </router-link>
      </template>
      <template #end>
        <div class="flex align-items-center">
          <Button 
            :icon="isDarkTheme ? 'pi pi-sun' : 'pi pi-moon'" 
            class="p-button-rounded p-button-text mr-2"
            @click="toggleTheme" 
            v-tooltip.bottom="isDarkTheme ? 'Switch to Light Mode' : 'Switch to Dark Mode'"
          />
          <Button 
            icon="pi pi-bell" 
            class="p-button-rounded p-button-text mr-2" 
            badge="2" 
            v-tooltip.bottom="'Notifications'"
          />
          <Button 
            icon="pi pi-user" 
            class="p-button-rounded p-button-text" 
            v-tooltip.bottom="'Profile'"
            @click="showProfileMenu"
          />
        </div>
      </template>
    </Menubar>
    
    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>

    <footer class="footer" :class="{ 'dark': isDarkTheme }">
      <div class="grid">
        <div class="col-12 md:col-4">
          <h3>AI-Ecosystem Platform</h3>
          <p>Empowering AI innovation with enterprise-grade tools</p>
        </div>
        <div class="col-12 md:col-4">
          <h4>Quick Links</h4>
          <ul>
            <li><router-link to="/tutorial">Documentation</router-link></li>
            <li><router-link to="/tutorial">Tutorials</router-link></li>
            <li><router-link to="/about">About Us</router-link></li>
          </ul>
        </div>
        <div class="col-12 md:col-4">
          <h4>Connect</h4>
          <div class="social-links">
            <a href="#" target="_blank"><i class="pi pi-github"></i></a>
            <a href="#" target="_blank"><i class="pi pi-twitter"></i></a>
            <a href="#" target="_blank"><i class="pi pi-linkedin"></i></a>
          </div>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2025 AI-Ecosystem Platform. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import Menubar from 'primevue/menubar';
import Button from 'primevue/button';
import Tooltip from 'primevue/tooltip';

export default {
  name: 'App',
  components: {
    Menubar,
    Button
  },
  directives: {
    tooltip: Tooltip
  },
  setup() {
    const isDarkTheme = ref(false);
    const menuItems = [
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
        label: 'Models',
        icon: 'pi pi-box',
        items: [
          {
            label: 'Model Registry',
            icon: 'pi pi-list',
            to: '/models/registry'
          },
          {
            label: 'Training',
            icon: 'pi pi-cog',
            to: '/models/training'
          },
          {
            label: 'Deployments',
            icon: 'pi pi-send',
            to: '/models/deployments'
          }
        ]
      },
      {
        label: 'Analytics',
        icon: 'pi pi-chart-bar',
        to: '/analytics'
      },
      {
        label: 'Help',
        icon: 'pi pi-question-circle',
        items: [
          {
            label: 'Documentation',
            icon: 'pi pi-file',
            to: '/documentation'
          },
          {
            label: 'Release History',
            icon: 'pi pi-history',
            to: '/releases'
          },
          {
            label: 'Support',
            icon: 'pi pi-comments',
            to: '/support'
          }
        ]
      }
    ];

    const toggleTheme = () => {
      isDarkTheme.value = !isDarkTheme.value;
      document.documentElement.setAttribute('data-theme', isDarkTheme.value ? 'dark' : 'light');
      localStorage.setItem('theme', isDarkTheme.value ? 'dark' : 'light');
    };

    const showProfileMenu = () => {
      // Implement profile menu logic
    };

    onMounted(() => {
      // Check saved theme preference
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme) {
        isDarkTheme.value = savedTheme === 'dark';
        document.documentElement.setAttribute('data-theme', savedTheme);
      } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        isDarkTheme.value = true;
        document.documentElement.setAttribute('data-theme', 'dark');
      }
    });

    return {
      isDarkTheme,
      menuItems,
      toggleTheme,
      showProfileMenu
    };
  }
}
</script>

<style lang="scss">
.layout-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--surface-ground);
}

.header {
  background: var(--surface-card);
  box-shadow: 0 2px 4px rgba(0,0,0,.1);

  .logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--text-color);
    text-decoration: none;
    display: flex;
    align-items: center;

    i {
      font-size: 1.8rem;
      color: var(--primary-color);
    }
  }
}

.main-content {
  flex: 1;
  padding: 2rem;
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
}

.footer {
  background: var(--surface-section);
  padding: 3rem 2rem 1rem;
  color: var(--text-color);

  h3, h4 {
    color: var(--primary-color);
    margin-bottom: 1rem;
  }

  ul {
    list-style: none;
    padding: 0;
    margin: 0;

    li {
      margin-bottom: 0.5rem;

      a {
        color: var(--text-color);
        text-decoration: none;
        transition: color 0.2s;

        &:hover {
          color: var(--primary-color);
        }
      }
    }
  }

  .social-links {
    display: flex;
    gap: 1rem;

    a {
      color: var(--text-color);
      font-size: 1.5rem;
      transition: color 0.2s;

      &:hover {
        color: var(--primary-color);
      }
    }
  }

  .footer-bottom {
    margin-top: 2rem;
    padding-top: 1rem;
    border-top: 1px solid var(--surface-border);
    text-align: center;
  }

  &.dark {
    background: var(--surface-card);
  }
}

// Transitions
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

// Global styles
body {
  margin: 0;
  font-family: var(--font-family);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--text-color);
}

* {
  box-sizing: border-box;
}

:root {
  --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
    Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
</style>
