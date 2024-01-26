<script>
  import { onMount } from "svelte";
  import { goto } from "$app/navigation";


    onMount(()=>{
        localStorage.removeItem("authTokens")
        goto("/login")
    })
   

</script>


