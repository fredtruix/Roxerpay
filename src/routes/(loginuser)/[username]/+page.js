// @ts-nocheck
import AuthStore from '../../../stores/auth';
import UserStore from '../../../stores/user';


let data = "";
let user_data = "";

AuthStore.subscribe((data) => {
    data = data;

})




UserStore.subscribe((user) => {
    user = user
})

export const load = async ({ fetch, params }) => {
    // console.log(params.username)



        let taskResponse = await fetch(`http://127.0.0.1:8000/task/${params.username}/`, {
            method: "GET",
            headers: { "Content-Type": "application/json" },
            'Authorization': `Bearer ${data.access}`,
        })
        const taskData = await taskResponse.json()
        // console.log(taskData)
        return taskData


 

}













// export const  load = async ({fetch}) => {
//     let taskResponse = await fetch(`http://127.0.0.1:8000/task/${user?.username}/`,{
//         method : "GET",
//         headers : { "Content-Type": "application/json" },
//         'Authorization': `Bearer ${data?.access}`,
//     })
//     const taskData = await taskResponse.json()
//     const task = taskData.data
//     return {
//        task
//     }
// }

