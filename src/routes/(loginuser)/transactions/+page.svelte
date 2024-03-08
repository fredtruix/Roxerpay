<script>
    import SideBar from "../../../components/SideBar.svelte";
    import TaskOption from "../../../components/TaskOption.svelte"
  //   import 

    //  export let data;
    //  const tasks = data.task;
     

</script>


<main class="mt-5">
  <!--Account profile Start-->
  <section class="py-lg-7 py-5 bg-light-subtle">
     <div class="container">
        <div class="row">
          <SideBar />

          <div class="col-lg-9 col-md-8">
            <TaskOption />
            <div class="mb-4">
               <h1 class="mb-0 h3">Ongoing task</h1>
            </div>
            <div class="card border-0 shadow-sm mb-4">
               <div class="card-body p-lg-5">
                

                  <ul class="list-group list-group-flush">
                     <li class="list-group-item px-0  ">
                        <div class="d-flex  mb-lg-0 align-items-lg-center">
                           <div class="icon-shape bg-twitter rounded icon-lg flex-shrink-0 mt-1">
                              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-twitter text-white" viewBox="0 0 16 16">
                                 <path
                                    d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z" />
                              </svg>
                           </div>
                           <div class="d-lg-flex w-100 ms-3 align-items-center">
                              <div class="mb-1">
                                 <h5 class="mb-1">Twitter  <span class="badge bg-light-subtle border border-light-subtle text-light-emphasis rounded-pill ms-1">on going</span><span class="badge bg-light-subtle border border-light-subtle text-light-emphasis rounded-pill ms-1">Recommend</span></h5>
                                 <small class="fs-7 mb-0">Automatically tweet when you get a coffee with a message. Your fans would love it!</small>
                              </div>
                             
                           </div>
                        </div>
                     </li>
                  
                  </ul>
               </div>
            </div>
            <div class="card border-0 shadow-sm mb-4">
                <div class="card-body p-lg-5">
                 
 
                   <ul class="list-group list-group-flush">
                      <li class="list-group-item px-0  ">
                         <div class="d-flex  mb-lg-0 align-items-lg-center">
                            <div class="icon-shape bg-twitter rounded icon-lg flex-shrink-0 mt-1">
                               <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-twitter text-white" viewBox="0 0 16 16">
                                  <path
                                     d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z" />
                               </svg>
                            </div>
                            <div class="d-lg-flex w-100 ms-3 align-items-center">
                               <div class="mb-1">
                                  <h5 class="mb-1">Twitter  <span class="badge bg-light-subtle border border-light-subtle text-light-emphasis rounded-pill ms-1">on going</span><span class="badge bg-light-subtle border border-light-subtle text-light-emphasis rounded-pill ms-1">Recommend</span></h5>
                                  <small class="fs-7 mb-0">Automatically tweet when you get a coffee with a message. Your fans would love it!</small>
                               </div>
                              
                            </div>
                         </div>
                      </li>
                   
                   </ul>
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