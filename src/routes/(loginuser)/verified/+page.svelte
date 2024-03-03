<script>
   import SideBar from "../../../components/SideBar.svelte";
   import TaskOption from "../../../components/TaskOption.svelte"
 //   import 

    export let data;
    const tasks = data.task;
    

</script>


<main class="mt-5">
   <!--Account profile Start-->
   <section class="py-lg-7 py-5 bg-light-subtle">
      <div class="container">
         <div class="row">
           <SideBar />
            <div class="col-lg-9 col-md-8">
             
                <TaskOption />
              
               <div class="row gy-lg-7 gy-5">
                  {#each tasks as task}
                  <article class="col-lg-3 col-md-6 col-6">
                     <a href="/task/{task.id}">
                     <figure class="mb-1 zoom-img">
                        
                           <img src="http://127.0.0.1:8000{task.task_image}" alt="blog" class="img-fluid rounded-3" width="100%" height="50" />
                 
                     </figure>
     
                     <a href="#!" class="badge  bg-primary-subtle text-primary-emphasis rounded-pill text-uppercase">NGN {task.amount.toFixed(2)}</a>
                     <h3 class=" fs-10 h4">
                        <small href="blog-single.html" class="text-reset fs-10">{task.title}</small>
                     </h3>
                     <div class="d-flex align-items-center justify-content-between mb-3 mb-md-0">
                        <div class="d-flex align-items-center">
                           <img src="http://127.0.0.1:8000{task.user_images}" alt="Avatar" class="avatar avatar-xs rounded-circle" />
                           <div class="ms-2">
                              <a href="#" class="text-reset fs-10">{task.username}</a>
                           </div>
                        </div>
                        <!-- <div class="ms-3"><span class="fs-10">{task.created}</span></div> -->
                   
                     </div>
                  </a>
                 
                  </article>
                  {/each}
           

                
                 
                  <div class="col-lg-12">
                     <div class="mt-xl-7 mt-3">
                        <a class="btn btn-outline-primary" href="#!">
                           <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                           <span class="ms-2">Load More</span>
                        </a>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </section>
   <!--Account profile end-->
</main>





<style>
 .fs-10{
    font-size: 12px;
    line-height: 18px;
 }
</style>