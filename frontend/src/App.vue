<template>
  <div class="layout-wrapper">
    <header class="header">
      <div class="logo">AI-Ecosystem</div>
      <nav class="nav-menu">
        <router-link to="/" class="nav-link">Home</router-link>
        <router-link to="/dashboard" class="nav-link">Dashboard</router-link>
        <router-link to="/about" class="nav-link">About</router-link>
      </nav>
    </header>
    
    <main class="main-content">
      <router-view />
    </main>

    <footer class="footer">
      <p>&copy; 2025 AI-Ecosystem. All rights reserved.</p>
    </footer>
  </div>
</template>

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
