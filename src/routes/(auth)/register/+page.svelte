<script>
  import {  redirect } from "@sveltejs/kit";
  import Theme from "../../../components/Theme.svelte";
  import { goto } from "$app/navigation";
  import toast from "svelte-french-toast";

  let username = "",
    email = "",
    password = "",
    comfirm_password = "",
    userError = "",
    emailError = "",
    comfromError = "",
    passwordError = "",
    status_code = "";

  const passwordConfrim = () => {
    if (password === comfirm_password) {
      status_code = "success";
      comfromError = "Correct matching password";
    } else {
      status_code = "danger";
      comfromError = "incorrect matching password";
      redirect(307, '/register')
    }
  };

  const submit = async () => {
    if (password === comfirm_password) {
      status_code = "success";
      comfromError = "Correct matching password";
    } else {
      status_code = "danger";
      comfromError = "incorrect matching password";
    }
    let response = await fetch("http://127.0.0.1:8000/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        username,
        email,
        password,
      }),
    });

    let data = await response.json();
    if (data.success == false ){
    if (data.data.username == undefined) {
      userError = "";
    } else {
      userError = data.data.username;
    }

    if (data.data.email == undefined) {
      emailError = "";
    } else {
      emailError = data.data.email;
    }

    if (data.data.password == undefined) {
      passwordError = "";
    } else {
      passwordError = data.data.password;
    }
    toast.error(data.message)

  }
  else{
    toast.success(data.message)
    goto("/login")
  }


    console.log(data); // Check the response data in the console

    // Other logic based on the response...

    // goto('/login')
  };
</script>

<main>
  <!--Pageheader start-->
  <div class="position-relative h-100">
    <div
      class="container d-flex flex-wrap justify-content-center align-items-center vh-100 w-lg-50 position-lg-absolute"
    >
      <div class="row justify-content-center">
        <div class="w-100 align-self-end col-12">
          <div class="text-center mb-7">
            <a href="index.html"
              ><img
                src="assets/images/logo/brand-icon.svg"
                alt="brand"
                class="mb-3"
              /></a
            >
            <h1 class="mb-1">Create Account</h1>
            <p class="mb-0">
              Sign up now and get free account instant. Already
              <a href="/login" class="text-primary">Sign in</a>
            </p>
          </div>

          <form
            on:submit|preventDefault={submit}
            class="needs-validation mb-6"
            
          >
            <div class="mb-4">
              <label for="signupEmailInput" class="form-label">
                Username <small class="text-danger">{userError}</small>
              </label>
              <input
                bind:value={username}
                type="username"
                class="form-control"
                required
              />

              <div class="mb-3">
                <label for="signupEmailInput" class="form-label">
                  Email <small class="text-danger">{emailError}</small>
                  <span class="text-danger"></span>
                </label>
                <input
                  bind:value={email}
                  type="email"
                  class="form-control"
                  required
                />
              </div>
              <div class="mb-3">
                <label for="formSignUpPassword" class="form-label"
                  >Password <small class="text-danger">{passwordError}</small
                  ></label
                >
                <div class="password-field">
                  <input
                    bind:value={password}
                    on:change={passwordConfrim}
                    type="password"
                    class="form-control"
                    required
                  />
                </div>
              </div>
              <div class="mb-3">
                <label for="formSignUpConfirmPassword" class="form-label"
                  >Confirm Password <small class="text-{status_code}"
                    >{comfromError}</small
                  ></label
                >
                <div class="password-field">
                  <input
                    bind:value={comfirm_password}
                    on:change={passwordConfrim}
                    type="password"
                    class="form-control"
                    required
                  />
                </div>
              </div>
              <div class="mb-3">
                <div class="d-flex align-items-center justify-content-between">
                  <div class="form-check">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      id="signupCheckTextCheckbox"
                      required
                    />
                    <label
                      class="form-check-label ms-2"
                      for="signupCheckTextCheckbox"
                    >
                      <a href="#">Terms of Use</a>
                      &
                      <a href="#">Privacy Policy</a>
                    </label>
                  </div>
                </div>
              </div>

              <div class="d-grid">
                <button class="btn btn-primary" type="submit">Sign Up</button>
              </div>
            </div>
          </form>

          <!-- <span>Sign up with your social network.</span>
          <div class="d-grid mt-3">
            <a href="#" class="btn btn-google">
              <span class="me-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-google"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M15.545 6.558a9.42 9.42 0 0 1 .139 1.626c0 2.434-.87 4.492-2.384 5.885h.002C11.978 15.292 10.158 16 8 16A8 8 0 1 1 8 0a7.689 7.689 0 0 1 5.352 2.082l-2.284 2.284A4.347 4.347 0 0 0 8 3.166c-2.087 0-3.86 1.408-4.492 3.304a4.792 4.792 0 0 0 0 3.063h.003c.635 1.893 2.405 3.301 4.492 3.301 1.078 0 2.004-.276 2.722-.764h-.003a3.702 3.702 0 0 0 1.599-2.431H8v-3.08h7.545z"
                  />
                </svg>
              </span>
              Continue with Google
            </a>
          </div>
          <div class="d-grid mt-2">
            <a href="#" class="btn btn-facebook">
              <span class="me-3">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="16"
                  height="16"
                  fill="currentColor"
                  class="bi bi-facebook"
                  viewBox="0 0 16 16"
                >
                  <path
                    d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"
                  />
                </svg>
              </span>
              Continue with Facebook
            </a>
          </div> -->

          <div class="text-center mt-7">
            <div class="small mb-3 mb-lg-0 text-body-tertiary">
              Copyright ©
              <span class="text-primary"
                ><a href="#">Block Bootstrap 5 Theme</a></span
              >
              | Designed by
              <span class="text-primary"><a href="#">CodesCandy</a></span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <slot />
  </div>
  <!--Pageheader end-->
  <!--sign up v2-->
  <div class="position-absolute start-0 bottom-0 m-4">
    <Theme />
  </div>
</main>

<style>
</style>
