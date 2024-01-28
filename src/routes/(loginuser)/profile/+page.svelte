<script>
  // @ts-nocheck

  import SideBar from "../../../components/SideBar.svelte";
  import UserStore from "../../../stores/user";
  import AuthStore from "../../../stores/auth";
  import toast from "svelte-french-toast";
  import { redirect } from '@sveltejs/kit';

  let first_name = "",
    last_name = "",
    phone = "",
    date_of_birth = "",
    address = "",
    user_id = "",
    access_token = "",
    username = "",
    avatar = "",
    email = "";

  AuthStore.subscribe((data) => {
    access_token = data?.access;
    // console.log(access_token)
  });

  UserStore.subscribe((data) => {
    first_name = data?.first_name;
    last_name = data?.last_name;
    username = data?.username;
    phone = data?.phone_number;
    date_of_birth = data?.date_of_birth;
    address = data?.address;
    user_id = data?.id;
    email = data?.email;
    avatar = data?.profile_image
  });


  let formData = new FormData()



  const displaySelectedImage = async (e) => {
   const fileInput = e.target
   
 

   if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();
        formData.append("profile_image", fileInput.files[0])
        formData.append("id",user_id)
        formData.append("email",email)
        formData.append("username",username)
        

        reader.onload = function(e) {
         let selectedImage = document.getElementById(image);
         selectedImage = e.target.result
        };
      

        reader.readAsDataURL(fileInput.files[0]);
    }

    let response = await fetch(`http://127.0.0.1:8000/user/${user_id}/`, {
      method: "PATCH",
      Authorization: `Bearer ${access_token}`,
      body: formData
    });

    let data = await response.json()
    if(data.success == false){
      toast.error("Profile image not uploaded successfully")
    }
    else{
      toast.success("Profile image uploaded successfully")
    }


   



  }

  const submit = async () => {
    let response = await fetch(`http://127.0.0.1:8000/user/${user_id}/`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      Authorization: `Bearer ${access_token}`,
      body: JSON.stringify({
        id: user_id,
        username,
        email,
        first_name,
        last_name,
        phone_number: phone,
        address,
      }),
    });

    let data = await response.json();
    if (data.success == false) {
      toast.error("Profile was not update successfully something went wrong");
    } else {
      setInterval(toast.success(data.message), 2000);

      console.log("happy");
    }
  };
</script>

<main>
  <!--Account profile Start-->
  <section class="py-lg-7 py-5 bg-light-subtle">
    <div class="container">
      <div class="row">
        <SideBar />
        <div class="col-lg-9 col-md-8">
          <div class="mb-4">
            <h1 class="mb-0 h3">{$UserStore?.username} Profile</h1>
          </div>
          <div class="card border-0 shadow-sm mb-4">
            <div class="card-body p-lg-5">
              <div class="mb-5">
                <h4 class="mb-1">Profile Picture</h4>
                <p class="mb-0 fs-6">
                  Upload a picture to make your profile stand out and let people
                  recognize your comments and contributions easily!
                </p>
              </div>
              {#key avatar}
              <div class="d-flex align-items-center">
                <img
                  id = "image"
                
                  src="http://127.0.0.1:8000{avatar}"
                
               
                  alt="avatar"
                  class="avatar avatar-lg rounded-circle"
                />
                <div class="ms-4">
                  <h5 class="mb-0">Your photo</h5>
                  <small
                    >Allowed *.jpeg, *.jpg, *.png, *.gif max size of 4 MB</small
                  >
                  <div class="badge rounded-pill bg-primary-subtle text-primary-emphasis">
                     <label class="form-label text-white m-1" for="customFile2">Choose file</label>
                     <input bind:value={avatar} type="file" class="form-control d-none" id="customFile2" on:change={displaySelectedImage} />
                  </div>
                </div>
              </div>
              {/key}
            </div>
          </div>
          <div class="card border-0 shadow-sm mb-4">
            <div class="card-body p-lg-5">
              <div class="mb-5">
                <h4 class="mb-1">Account Information</h4>
                <p class="mb-0 fs-6">
                  Edit your personal information and address.
                </p>
              </div>
              <form
                on:submit|preventDefault={submit}
                class="row g-3 needs-validation"
                novalidate
              >
                <div class="col-lg-6 col-md-12">
                  <label for="profileFirstNameInput" class="form-label"
                    >First Name</label
                  >
                  <input
                    type="text"
                    class="form-control"
                    id="profileFirstNameInput"
                    bind:value={first_name}
                    required
                  />
                  <div class="invalid-feedback">Please enter firstname.</div>
                </div>
                <div class="col-lg-6 col-md-12">
                  <label for="profileLastNameInput" class="form-label"
                    >Last Name</label
                  >
                  <input
                    type="text"
                    class="form-control"
                    id="profileLastNameInput"
                    bind:value={last_name}
                    required
                  />
                  <div class="invalid-feedback">Please enter lastname.</div>
                </div>
                <div class="col-lg-6">
                  <label for="profilePhoneInput" class="form-label">Phone</label
                  >
                  <input
                    type="text"
                    class="form-control input-phone"
                    id="profilePhoneInput"
                    bind:value={phone}
                    required
                  />
                </div>
                <div class="col-lg-6">
                  <label for="profileBirthdayInput" class="form-label"
                    >Date of birth</label
                  >
                  <input
                    type="date"
                    class="form-control input-date"
                    bind:value={date_of_birth}
                    id="profileBirthdayInput"
                    required
                  />
                </div>
                <div class="col-lg-12">
                  <label for="profileAddressInput" class="form-label"
                    >Address Line</label
                  >
                  <input
                    type="text"
                    class="form-control"
                    id="profileAddressInput"
                    bind:value={address}
                    required
                  />
                </div>

                <div class="col-12 mt-4">
                  <button class="btn btn-primary me-2" type="submit"
                    >Save Changes</button
                  >
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!--Account profile end-->
</main>
