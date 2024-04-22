<script>
  // @ts-nocheck

  import SideBar from "../../../components/SideBar.svelte";
  import TaskOption from "../../../components/TaskOption.svelte";
  import UserStore from "../../../stores/user";

  let username = "",
    option = "handler",
    owners_data = "",
    new_data = "";

  UserStore.subscribe((data) => {
    username = data;
  });

  // console.log(username)

  // console.log(new_data)

  fetch(
    `http://127.0.0.1:8000/task/transaction/${username.username}/handler/`,
    {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    }
  )
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      new_data = data.data;
    });

  fetch(`http://127.0.0.1:8000/task/transaction/${username.username}/owner/`, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      owners_data = data.data;
    });
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
            <h1 class="mb-0 h3">Ongoing task you are in</h1>
          </div>

          {#each new_data as task}
        <a href="/transactions/{task.id}">
         <div class="card border-0 shadow-sm mb-4">
            <div class="card-body p-lg-1">

              <ul class="list-group list-group-flush mx-4">
                <li class="list-group-item px-0 py-4">
                   <div class="d-flex mb-3 mb-lg-0 align-items-lg-center">
                      <!-- <div class="icon-shape bg-twitter rounded icon-lg flex-shrink-0 mt-1">
                         <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-twitter text-white" viewBox="0 0 16 16">
                            <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"></path>
                         </svg>
                      </div> -->
                      <div class="d-lg-flex w-100 ms-3 align-items-center">
                         <div class="">
                            <h5 class="mb-1">{task.title} by {task.task_owner_name}</h5>
                            <p class="fs-6 mb-0">{task.description.substr(0, 80)}.... </p>
                            {#if task.pay == true}
                            <span
                              class="badge bg-primary-subtle border border-light-subtle text-light-emphasis rounded-pill "
                              >Payment on standby</span
                            >
                            {:else}
                            <span
                            class="badge bg-danger-subtle border border-light-subtle text-danger-emphasis rounded-pill "
                            >Payment not on standby</span
                          >
                            {/if}
                            <span
                            class="badge bg-secondary-subtle border border-light-subtle text-warning-emphasis rounded-pill ms-1"
                            >Period {task.period} {task.number}</span
                          >
                         </div>
                     
                      </div>
                   </div>
                </li>
               
             </ul>
             
            </div>
          </div></a>
          {/each}

          <div class="mb-4">
            <h1 class="mb-0 h3 fs-7 ">Ongoing task you created</h1>
          </div>

          {#each owners_data as task}
           <a href="/transactions/{task.id}">
            <div class="card border-0 shadow-sm mb-2">
               <div class="card-body p-lg-1">
                <ul class="list-group list-group-flush mx-4">
                  <li class="list-group-item px-0 py-4">
                     <div class="d-flex mb-3 mb-lg-0 align-items-lg-center">
                        <!-- <div class="icon-shape bg-twitter rounded icon-lg flex-shrink-0 mt-1">
                           <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-twitter text-white" viewBox="0 0 16 16">
                              <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"></path>
                           </svg>
                        </div> -->
                        <div class="d-lg-flex w-100 ms-3 align-items-center">
                           <div class="">
                              <h5 class="mb-1">{task.title} by {task.task_owner_name}</h5>
                              <p class="fs-6 mb-0">{task.description.substr(0, 80)}.... </p>
                              {#if task.pay == true}
                              <span
                                class="badge bg-primary-subtle border border-light-subtle text-light-emphasis rounded-pill "
                                >Payment on standby</span
                              >
                              {:else}
                              <span
                              class="badge bg-danger-subtle border border-light-subtle text-danger-emphasis rounded-pill "
                              >Payment not on standby</span
                            >
                              {/if}
                              <span
                              class="badge bg-secondary-subtle border border-light-subtle text-warning-emphasis rounded-pill ms-1"
                              >Period {task.period} {task.number}</span
                            >
                           </div>
                       
                        </div>
                     </div>
                  </li>
                 
               </ul>
               </div>
             </div>
           </a>
          {/each}
        </div>
      </div>
    </div>
  </section>
  <!--Account profile end-->
</main>

<style>
  .fs-10 {
    font-size: 12px;
    line-height: 18px;
  }
</style>
