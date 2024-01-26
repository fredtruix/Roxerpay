<script>
 import Navbar from "../../components/Navbar.svelte";
 import toast, { Toaster } from 'svelte-french-toast';
 import Footer from "../../components/Footer.svelte";
</script>

<Navbar />
<Toaster />
<slot />


