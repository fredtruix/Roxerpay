<script>
  // @ts-nocheck

  import SideBar from "../../../../../components/SideBar.svelte";
  import toast from "svelte-french-toast";
  import { goto } from "$app/navigation";

  import AuthStore from "../../../../../stores/auth";
  import UserStore from "../../../../../stores/user";

  export let data;
  let task = data.data;

  let taskImage = task.task_image,
    title = task.title,
    description = task.description,
    amount = task.amount,
    user_id = "",
    access_token = "",
    automaticPay = task.pay,
    display_image = `http://127.0.0.1:8000${task.task_image}`,
    verifiedUser = task.verified_or_unverified,
    partakers = task.partakers;
    let check_image = "";

  const onFileSelected = (e) => {
    let image = e.target.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(image);
    reader.onload = (e) => {
      taskImage = image;
      display_image = e.target.result;
      check_image = e.target.result;
    };
    console.log(typeof(display_image))
  };

  console.log(typeof(display_image))

  const handlepay = () => {
    automaticPay = !automaticPay;
    console.log(automaticPay);
  };

  const handleveryfity = () => {
    verifiedUser = !verifiedUser;
  };

  let new_data = "";
  let new_user = "";

  AuthStore.subscribe((data) => {
      new_data  = data;
    access_token = new_data?.access
  });



  UserStore.subscribe((user) => {
    user = user;
    user_id = user?.id
    new_user = user;

  });


    console.log(new_data)
  let formData = new FormData();

  const handleSubmit = async () => {
    if (verifiedUser === true || verifiedUser == "verified") {
      verifiedUser = "verified";
    } else {
      verifiedUser = "both";
    }
    if (check_image === display_image){
     formData.append("task_image", taskImage)
    
    }
    else{
     
    }
    formData.append("username_id", Number(user_id))
    formData.append("title", title)
    formData.append("description", description)
    formData.append("verified_or_unverified", verifiedUser)
    formData.append("pay", automaticPay)
    formData.append("amount", Number(amount))
    formData.append("partakers", partakers)
    let taskResponse = await fetch(`http://127.0.0.1:8000/task/detail/${task.id}/`, {
      method: "PATCH",
      Authorization: `Bearer ${access_token}`,
      body: formData
    });
    let res = await taskResponse.json()
    if (res.success == true){
      toast.success(res.message)
     goto(`/task/${res.data.id}`)
       

    }
    else{
      toast.error(res.message)
    }
  };
</script>

 <main class="mt-5">
    <section class="py-lg-7 py-5 bg-light-subtle">
      <div class="container">
        <div class="row">
          <SideBar />
          <div class="col-lg-9 col-md-8">
            <div class="mb-4">
              <h1 class="mb-0 h3">Update</h1>
            </div>
  
            <div class="card border-0 shadow-sm mb-4">
              <div class="card-body p-lg-5">
                <div class="mb-5">
                  <h4 class="mb-1">Update task Information and Description</h4>
                  <p class="mb-0 fs-6">You decide are you want your task.</p>

                  <figure class="">
                    <img
                      src={display_image}
                      alt="events"
                      class="rounded-3 border my-4"
                      width="100%"
                    />
                  </figure>
                </div>
                <form class="row g-3 needs-validation">
                  <div class="col-lg-12 col-md-12">
                    <label for="profileFirstNameInput" class="form-label"
                      >Task Image</label
                    >
                    <input
                      type="file"
                      class="form-control"
                      id="profileFirstNameInput"
                      bind:value={taskImage}
                      accept=".jpg, .jpeg, .png"
                      on:change={(e) => onFileSelected(e)}
                    />
                  </div>
  
                  <div class="col-lg-12 col-md-12">
                    <label for="profileFirstNameInput" class="form-label"
                      >Title</label
                    >
                    <input
                      type="text"
                      class="form-control"
                      id="profileFirstNameInput"
                      bind:value={title}
                      required=""
                    />
                  </div>
                  <div class="col-lg-12 col-md-12">
                    <label for="profileLastNameInput" class="form-label"
                      >Description</label
                    >
  
                    <textarea
                      class="form-control"
                      id="textarea-input"
                      rows="5"
                      required
                      bind:value={description}
                    />
                  </div>
  
                  <div class="col-lg-6 col-md-12">
                    <input
                      type="number"
                      class="form-control"
                      id="profileFirstNameInput"
                      placeholder="Amount"
                      required=""
                      bind:value={amount}
                    />
                  </div>
  
                  <div class="col-lg-6 col-md-12">
                    <input
                      type="number"
                      class="form-control"
                      id="profileFirstNameInput"
                      placeholder="Numbers of user"
                      required=""
                      bind:value={partakers}
                    />
                  </div>
                  <div class="col-lg-3 mx-2 col form-check form-switch mt-4">
                    <label for="profilePhoneInput" class="form-label"
                      >Automatic pay</label
                    >
                    <input
                      class="form-check-input"
                      type="checkbox"
                      role="switch"
                      id="flexSwitchCheckChecked"
                      on:input={handlepay}
                    />
                  </div>
                  <div class="col-lg-3 col form-check form-switch mt-4">
                    <label for="profilePhoneInput" class="form-label"
                      >Verified user</label
                    >
                    <input
                      class="form-check-input"
                      type="checkbox"
                      role="switch"
                      id="flexSwitchCheckChecked"
                      on:input={handleveryfity}
                    />
                  </div>
                  {#if taskImage === "" || title === "" || description === "" || amount === "" || partakers == 0}
                    <div class="col-12 mt-4 d-grid">
                      <button
                        class="btn btn-primary me-2"
                        on:click={() => {
                          toast.error("Please add all required fields");
                        }}
                        type="button">Preview</button
                      >
                    </div>
                  {:else}
                    <div class="col-12 mt-4 d-grid">
                      <button
                        class="btn btn-primary me-2"
                        data-bs-toggle="modal"
                        data-bs-target="#exampleModalLong"
                        type="submit">Preview</button
                      >
                    </div>
                  {/if}
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  
    <div
      class="modal fade"
      id="exampleModalLong"
      tabindex="-1"
      aria-labelledby="exampleModalLongLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLongLabel">
              Task preview
            </h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body" style="">
            <h3>{title}</h3>
            <figure class="">
              <img
                src={display_image}
                alt="events"
                class="rounded-3 border my-4"
                width="100%"
              />
            </figure>
            <p>{description}</p>
            <li class="list-group-item py-4 px-0">
              <h5 class="">
                <span
                  class="badge bg-primary-subtle text-primary-emphasis rounded-pill text-uppercase m-1"
                  >Price NGN {parseFloat(amount).toFixed(2)}</span
                >
                {#if automaticPay === "false"}
                  <span
                    class="badge bg-secondary text-danger rounded-pill text-uppercase m-1"
                    >Payment not automatic</span
                  >
                {:else}
                  <span
                    class="badge bg-secondary text-danger rounded-pill text-uppercase m-1"
                    >Payment automatic</span
                  >
                {/if}
  
                {#if verifiedUser === false}
                <h1> </h1>
                {:else}
                <span
                  class="badge bg-warning text-light rounded-pill text-uppercase m-1"
                  >verified account</span
                >
                {/if}
                <span
                class="badge bg-warning text-light rounded-pill text-uppercase m-1"
                >task engagers {partakers}</span
              >
              </h5>
            </li>
          </div>
          <div class="d-grid">
            <button
              type="button"
              class="btn btn-primary mx-3 my-3" data-bs-dismiss="modal"
              on:click={handleSubmit}>Submit</button
            >
          </div>
        </div>
      </div>
    </div>
  </main> 
