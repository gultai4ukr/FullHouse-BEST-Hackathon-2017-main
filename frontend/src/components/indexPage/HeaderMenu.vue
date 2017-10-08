<template>
  <div class="headerMenu">
    <img src="../../icons/logo.svg" class="Combined-Shape"><font class="Billio">Bill.io</font> 
      <router-link class="link" to="/categories">Categories</router-link>
      <router-link class="link" to="/hotels">Hotels</router-link>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
  .headerMenu {
    width: 100%;
  }
  a {
    font-family: Montserrat;
    text-decoration: none;
    color: #fff;
    font-size: 1.1rem;
    margin-left: 4%;
  }
  .Billio {
  width: 79px;
  height: 27px;
  font-family: Montserrat;
  font-size: 32px;
  font-weight: 600;
  line-height: 0.84;
  letter-spacing: -1.8px;
  text-align: center;
  color: #ffffff;
}

.link:hover {
  border-bottom: 2px solid;
}
</style>
