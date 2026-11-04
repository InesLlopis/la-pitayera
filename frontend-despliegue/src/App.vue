<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>
<template>
  <header class="app-header">
    <nav>
      <RouterLink to="/">Inicio</RouterLink>
      <RouterLink to="/hello">Hello</RouterLink>
    </nav>
  </header>

  <main class="app-main">
    <RouterView />
  </main>
</template>

<style scoped>
:focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 3px;
}
  .app-header {
    padding: var(--space-m) var(--space-l);
    background: var(--color-primary);
  }
  nav {
    display: flex;
    gap: var(--space-l);
  }
  nav a {
    color: var(--color-on-primary);
    text-decoration: none;
  }
  nav a.router-link-exact-active {
    text-decoration: underline;
  }
  .app-main {
    padding: var(--space-l);
  }
</style>