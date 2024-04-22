<script>
  // @ts-nocheck
  import SideBar from "../../../../components/SideBar.svelte";
  //  import TaskOption from "../../../../components/TaskOption.svelte";
  import UserStore from "../../../../stores/user";
  import toast from "svelte-french-toast";
  import { goto } from "$app/navigation";

  export let data;
  let task = data.data;
  let username = "";
  // console.log(task);

  UserStore.subscribe((user) => {
    user = user;
    username = user.username
    // console.log(user);
  });

  const handleDelete = async (task_id) => {
    let taskResponse = await fetch(
      `http://127.0.0.1:8000/task/detail/${task_id}/`,
      {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        //   'Authorization': `Bearer ${data.access}`,
      }
    );

    const taskData = await taskResponse.json()
    const task = taskData
    console.log(task.message)
    if (task.success == true){
      toast.success(task.message)
      goto('/task')
    }
    else{
      toast.error(task.message)
    }
   
  };


  const accept = async () =>{
    let acceptResponse = await fetch(
      `http://127.0.0.1:8000/task/accept/`,
      {
        method : "POST",
        headers: { "Content-Type": "application/json" },
        body : JSON.stringify(
          {
            task_owner : task.id,
            task_owner_name : task.username,
            task_handler : username,
            title : task.title,
            description : task.description,
            pay : task.pay,
            amount : task.amount,
            period : task.period,
            number : task.number
          }

        )
      }
    )
  }
</script>

<main class="mt-5">
  <!--Account profile Start-->
  <section class=" py-5 bg-light-subtle">
    <div class="container">
      <div class="row">
        <SideBar />
        <div class="col-lg-9 col-md-8">
          <!-- <TaskOption /> -->

          <div class="row gy-5">
            <section class="mb-xl-9">
              <div class="container">
                <div class="row">
                  <div class="col-md-12">
                    <div class="mb-6">
                      <h2 class="mb-0">
                        <img
                          src="http://127.0.0.1:8000{task.user_images}"
                          alt="avatar"
                          class="avatar avatar-lg rounded-circle mx-2"
                        />{task.username} created Task {task.title}
                      </h2>
                    </div>
                  </div>
                </div>

                <div class="row">
                  <div class="col-lg-10 col-md-12">
                    <figure>
                      <img
                        src="http://127.0.0.1:8000{task.task_image}"
                        class="img-fluid rounded-3 shadow-sm"
                        alt="events"
                      />
                    </figure>
                  </div>
                </div>
                <div class="row">
                  <div class="col-lg-10 col-md-12 order-2">
                    <div class="mb-6 mt-4">
                      <p class="mb-3"></p>
                    </div>

                    <ul class="list-group list-group-flush mb-0">
                      <li class="list-group-item pb-4 px-0">
                        <h5>
                          <span>{new Date(task.created)}</span>
                        </h5>
                      </li>
                      <li class="list-group-item py-4 px-0">
                        <h5>
                          <span
                            class="badge bg-primary-subtle text-primary-emphasis rounded-pill text-uppercase m-1"
                            >Price NGN {task.amount.toFixed(2)}</span
                          >
                          <span
                            class="badge bg-info text-light rounded-pill text-uppercase m-1"
                            >Payment {#if task.pay == true}
                              automatic
                            {:else}
                              manual
                            {/if}</span
                          >
                          <span
                            class="badge bg-warning text-light rounded-pill text-uppercase m-1"
                            >{task.verified_or_unverified} users</span
                          >
                          <span
                            class="badge bg-success text-light rounded-pill text-uppercase m-1"
                            >{task.partakers} engagers needed for task</span
                          >

                          <span
                          class="badge bg-danger text-light rounded-pill text-uppercase m-1"
                          >Period:  {task.number} {task.period}s</span
                        >
                        </h5>
                        <p class="mb-0">{task.description}</p>
                      </li>
                    </ul>

                    <div>
                      {#if $UserStore?.id === task.username_id}
                        <div class="card shadow-sm">
                          <div class="card-body">
                            <div class="mb-6 text-center">
                              <h3 class="mb-0">This task was created by you</h3>
                              <div class=" gap-2 m-4">
                                <a
                                  href="update/{task.id}"
                                  type="button"
                                  class="btn btn-primary px-5 m-2">Update task <i class='bx bxs-add-to-queue'></i></a
                                >
                                <button
                                  type="button"
                                  class="btn btn-danger px-5 m-2 " data-bs-toggle="modal"
                                  data-bs-target="#exampleModal"
                                >Delete Task <i class='bx bxs-trash-alt'></i></button
                                >
                              </div>
                            </div>

                            <!-- <div class="d-grid">
                                          <button class="btn btn-primary" type="submit">Accept task</button>
                                       </div> -->
                          </div>
                        </div>
                      {:else}
                        <div class="card shadow-sm">
                          <div class="card-body">
                            <div class="mb-6 text-center">
                              <h3 class="mb-0">
                                Click accept Button to accept task
                              </h3>
                            </div>

                            <div class="d-grid">
                              <button on:click={accept} class="btn btn-primary" type="submit"
                                >Accept task</button
                              >
                            </div>
                          </div>
                        </div>
                      {/if}
                    </div>
                  </div>
                </div>
              </div>
            </section>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!--Account profile end-->
</main>


<!--modal-->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel"
  aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Delete</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal"
          aria-label="Close"></button>
      </div>
      <div class="modal-body">
       Are you sure you want to delete task "{task.title}"
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="modal">cancel <i class='bx bx-arrow-back'></i></button>
        <button type="button" class="btn btn-danger btn-sm" data-bs-dismiss="modal"  on:click={()=>{handleDelete(task.id)}}>Delete <i class='bx bx-trash'></i></button>
      </div>
    </div>
  </div>
</div>

<style>
  .fs-10 {
    font-size: 12px;
    line-height: 18px;
  }
</style>
