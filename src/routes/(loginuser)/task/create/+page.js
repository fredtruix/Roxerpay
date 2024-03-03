// @ts-nocheck
import AuthStore from '../../../../stores/auth.js'

let data = "";

AuthStore.subscribe((data) =>{
    data = data;
})


// export const  load = async ({fetch}) => {
//     let taskResponse = await fetch('http://127.0.0.1:8000/task/create/',{
//         method : "POST",
//         headers : { "Content-Type": "application/json" },
//         'Authorization': `Bearer ${data.access}`,
//     })
//     const taskData = await taskResponse.json()
//     const task = taskData.data
//     return {
//        task
//     }
// }