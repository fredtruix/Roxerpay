<script>
      import SideBar from "../../../components/SideBar.svelte";
   //  import TaskOption from "../../../../components/TaskOption.svelte";
 

</script>


<main class="mt-5">
    <!--Avcount appearance start-->
    <section class="py-lg-7 py-5 bg-light-subtle">
       <div class="container">
          <div class="row">
            <SideBar />
             <div class="col-lg-3 col-md-4">
                <div class="d-flex d-md-none justify-content-center my-5">
                    <!--Checkbox and radio-->
                    <div class="btn-group btn-group-lg" role="group" aria-label="large  toggle button group">
                       <a href="/task" class="btn btn-primary " aria-current="page"><i class='bx bx-task '></i></a>
                       <a href="/profile" class="btn btn-primary"><i class='bx bx-user'></i></a>
                       <a href="/account" class="btn btn-primary  px-5"><i class='bx bx-home'></i></a>
                       <a href="#" class="btn btn-primary"><i class='bx bxs-circle-three-quarter'></i></a>
                       <a href="#" class="btn btn-primary"><i class='bx bxs-credit-card-front'></i></a>
                     </div>
                 </div >
             </div>
             <div class="col-lg-6 col-md-6">
                <div class="mb-4">
                   <h1 class="mb-0 h3">Create task</h1>
                </div>
                <div class="card border-0 shadow-sm mb-4">
                   <div class="card-body p-lg-5">
                    
                     
                      <form>
                         <div class="row">
                            <div class="col-lg-6 mb-4 mb-lg-0">
                               <div class="card h-100">
                                  <div class="card-header bg-white">
                                     <div class="form-check">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioLight" checked />
                                        <label class="form-check-label" for="flexRadioLight">
                                           <span class="fw-semibold fs-5 text-dark ms-1">Light Theme</span>
                                        </label>
                                     </div>
                                  </div>
                                  <div class="card-body">
                                     <p class="card-text fs-6 mb-4">This theme will be active when your system is set to “light mode”</p>
                                     <img src="assets/images/landings/account/light.svg" alt="light" class="w-100" />
                                  </div>
                               </div>
                            </div>
                            <div class="col-lg-6 mb-4 mb-lg-0">
                               <div class="card h-100">
                                  <div class="card-header bg-white">
                                     <div class="form-check">
                                        <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDark" />
                                        <label class="form-check-label" for="flexRadioDark">
                                           <span class="fw-semibold fs-5 text-dark ms-1">Dark Theme</span>
                                        </label>
                                     </div>
                                  </div>
                                  <div class="card-body">
                                     <p class="card-text fs-6">This theme will be active when your system is set to “dark mode”</p>
                                     <img src="assets/images/landings/account/dark.svg" alt="dark" class="w-100" />
                                  </div>
                               </div>
                            </div>
                         </div>
                      </form>
                   </div>
                </div>
             </div>
          </div>
       </div>
    </section>
    <!--Avcount appearance end-->
 </main>



<style>

</style>