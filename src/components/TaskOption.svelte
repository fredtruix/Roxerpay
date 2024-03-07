<script>
// @ts-nocheck

   import UserStore from "../stores/user";

</script>

<div class="row mb-5">
    <!-- <div class="col-lg-8 col-md-8 col-12">
       <div class="row g-2 g-sm-3 align-items-center">
          <div class="col-lg-8 col-md-8 col-12">
             <form>
                <label for="searchInput" class="form-label visually-hidden">Search Blog</label>
                <input type="search" class="form-control" id="searchInput" placeholder="Search Blog" />
             </form>
          </div>
          <div class="col-lg-4 col-md-4 col-12">
             <label for="categoryList" class="form-label visually-hidden">Search Category</label>
             <select class="form-select" id="categoryList">
                <option selected disabled value="">Select Category</option>
                <option value="Digital">Digital</option>
                <option value="Design">Design</option>
                <option value="Business">Business</option>
                <option value="Startup">Startup</option>
             </select>
          </div>
       </div>
    </div> -->
    <div class="col-lg-4 col-md-4 col-12 ">
       <ul class="nav d-flex gap-1 justify-content-md-start mt-3 mt-md-0">
           <li>
               <a class="btn btn-secondary  btn-sm" href="/task">
                   all
          
               </a>
            </li>
          <li>
             <a class="btn btn-light  btn-sm" href="/verified">
               verified
          
             </a>
          </li>

          <li>
            <a class="btn btn-light  btn-sm" href="/{$UserStore?.username}">
             My task
         
            </a>
         </li>
         <li>
            <a class="btn btn-light  btn-sm" href="/transactions">
             On going task
         
            </a>
         </li>
      
       </ul>
    </div>
 </div>