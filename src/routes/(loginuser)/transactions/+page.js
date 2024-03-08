// @ts-nocheck
import AuthStore from "../../../stores/auth";
import UserStore from "../../../stores/user";


let new_data = "";
let new_user = ""

AuthStore.subscribe((data) => {
    data = data;
    new_data = data
})

UserStore.subscribe((user) => {
    new_user = user

})









export const load = async ({ fetch }) => {

 


        // let taskResponse =  fetch(`http://127.0.0.1:8000/task/transaction/${new_user.username}/owner/`, {
        //     method: "GET",
        //     headers: { "Content-Type": "application/json" },
        //     'Authorization': `Bearer ${new_user.access}`,
        // })
        // const taskData = await taskResponse.json()
        // // console.log(taskData)
        // return taskData
    
   

       


 

}