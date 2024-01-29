<script>
  // @ts-nocheck

  import Theme from "../../../components/Theme.svelte";
  import toast from "svelte-french-toast";
  import AuthStore from "../../../stores/auth";
  import { goto } from "$app/navigation";

  let email = "",
    password = "";

  const submit = async () => {
    let response = await fetch("http://127.0.0.1:8000/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        email,
        password,
      }),
    });

    let data = await response.json();
    if (response.status === 200) {
      localStorage.setItem("authTokens", JSON.stringify(data));
      let localData = localStorage.getItem("authTokens");

      AuthStore.update((data) => (data = JSON.parse(localData)));

      toast.success("Login successful");

      goto("/task");
    } else {
      toast.error(data.detail);
    }
  };
</script>

<main>
  <!--Pageheader start-->
  <div class="position-relative h-100">
    <div
      class="container d-flex flex-wrap justify-content-center vh-100 align-items-center w-lg-50 position-lg-absolute"
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
            <h1 class="mb-1">Welcome Back</h1>
            <p class="mb-0">
              Don’t have an account yet?
              <a href="/register" class="text-primary">Register here</a>
            </p>
          </div>
          <form on:submit|preventDefault={submit} class="needs-validation mb-6">
            <div class="mb-3">
              <label for="signinEmailInput" class="form-label"> Email </label>
              <input
                bind:value={email}
                type="email"
                class="form-control"
                id="signinEmailInput"
                required
              />
              <div class="invalid-feedback">Please enter email.</div>
            </div>
            <div class="mb-3">
              <label for="formSignUpPassword" class="form-label">Password</label
              >
              <div class="password-field position-relative">
                <input
                  bind:value={password}
                  type="password"
                  class="form-control fakePassword"
                  id="formSignUpPassword"
                  required
                />
                <span><i class="bi bi-eye-slash passwordToggler"></i></span>
                <div class="invalid-feedback">Please enter password.</div>
              </div>
            </div>

            <div class="mb-3">
              <div class="d-flex align-items-center justify-content-between">
                <div>
                  <a href="forget-password-v2.html" class="text-primary"
                    >Forgot Password</a
                  >
                </div>
              </div>
            </div>

            <div class="d-grid">
              <button class="btn btn-primary" type="submit">Sign In</button>
            </div>
          </form>

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
    <!--Pageheader end-->
    <!--Sign up v2 start-->
    <div class="position-absolute start-0 bottom-0 m-4">
      <Theme />
    </div>
    <!--Sign up v2 end-->
  </div>
</main>
