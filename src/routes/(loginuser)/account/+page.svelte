<script>
// @ts-nocheck

    import SideBar from "../../../components/SideBar.svelte";
    import AuthStore from "../../../stores/auth";
    import UserStore from "../../../stores/user";
    import { jwtDecode } from "jwt-decode";

   // let user = "";
   //  AuthStore.subscribe(data =>{
   //    return data
   //  })

 




 
</script>

<main class="my-5">
    <!--Account home start-->
    <section class="py-lg-7 py-5 bg-light-subtle my-5">
       <div class="container">
          <div class="row">
             <SideBar />
             <div class="col-lg-9 col-md-8">
                <div class="mb-4">
                   <h1 class="mb-0 h3">Hey, {$UserStore?.username}!</h1>
                 
                </div>
                <div class="mb-5">
                   <a href="/task/create" type="button" class="btn btn-primary ml">Create Task <i class='bx bx-task mx-1'></i></a>
                </div>
                <div class="row mb-5 g-4">
                   <div class="col-lg-4 col-md-6">
                      <div class="card border-0 shadow-sm">
                         <div class="card-body">
                            <span>Balance</span>
                            <h3 class="mb-0 mt-4">NGN {$UserStore?.wallet.toFixed(2)}</h3>
                         </div>
                      </div>
                   </div>
                   <div class="col-lg-4 col-md-6">
                      <div class="card border-0 shadow-sm">
                         <div class="card-body">
                            <span>Past 7 days</span>
                            <h3 class="mb-0 mt-4">NGN 4356</h3>
                         </div>
                      </div>
                   </div>
                   <div class="col-lg-4 col-md-6">
                      <div class="card border-0 shadow-sm">
                         <div class="card-body">
                            <span>Total Earnings</span>
                            <h3 class="mb-0 mt-4">NGN {$UserStore?.task_earning.toFixed(2)}</h3>
                         </div>
                      </div>
                   </div>
                </div>

                <div class="mb-3">
                   <h4 class="mb-0">More ways to earn</h4>
                </div>
                <div class="row g-4">
                   <div class="col-lg-4 col-md-6">
                      <div class="card border-0 shadow-sm">
                         <div class="card-body">
                            <div class="mb-4">
                              <i class='bx bxs-credit-card-front display-5 text-primary'></i>
                            </div>
                            <div class="mb-4">
                               <h5 class="mb-2">Deposit</h5>
                               <p class="mb-0 pe-xl-7">Deposit funds into your account to create Task</p>
                            </div>

                            <a href="#" class="icon-link icon-link-hover text-inherit">
                               Make deposit
                               <i class='bx bxs-credit-card-front'></i>
                            </a>
                         </div>
                      </div>
                   </div>
                   <div class="col-lg-4 col-md-6">
                      <div class="card border-0 shadow-sm">
                         <div class="card-body">
                            <div class="mb-4">
                              <i class='bx bx-task display-5 text-primary' ></i>
                            </div>
                            <div class="mb-4">
                               <h5 class="mb-2">My Task</h5>
                               <p class="mb-0">See all my task and complete</p>
                            </div>

                            <a href="/{$UserStore?.username}" class="icon-link icon-link-hover text-inherit">
                               Check task
                               <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                  <path
                                     fill-rule="evenodd"
                                     d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"></path>
                               </svg>
                            </a>
                         </div>
                      </div>
                   </div>
                   <div class="col-lg-4 col-md-6">
                      <div class="card border-0 shadow-sm">
                         <div class="card-body">
                            <div class="mb-4">
                              <i class='bx bxs-gift display-5 text-primary'></i>
                            </div>
                            <div class="mb-4">
                               <h5 class="mb-2">Roxaearn</h5>
                               <p class="mb-0">Direct Task from Roxaearn</p>
                            </div>

                            <a href="#" class="icon-link icon-link-hover text-inherit">
                                Task from roxa
                               <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="currentColor" class="bi bi-arrow-right" viewBox="0 0 16 16">
                                  <path
                                     fill-rule="evenodd"
                                     d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"></path>
                               </svg>
                            </a>
                         </div>
                      </div>
                   </div>
                </div>
             </div>
          </div>
       </div>
    </section>
    <!--Account home end-->
 </main>