<script>
  import toast, { Toaster } from 'svelte-french-toast';
</script>
<Toaster />
<slot></slot>
<div
      class="position-fixed top-0 end-0 w-50 h-100 d-none d-xl-block vh-100"
      style="background-image: url(assets/images/sign-in/authentication-img.jpg); background-position: center; background-repeat: no-repeat; background-size: cover"
    >
   </div>