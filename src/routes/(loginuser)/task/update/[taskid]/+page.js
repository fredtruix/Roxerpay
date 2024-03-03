// @ts-nocheck
import AuthStore from '../../../../../stores/auth';



let data = "";

AuthStore.subscribe((data) => {
    data = data;
})

export const load = async ({ fetch, params }) => {
    console.log(params.taskid)



    let taskResponse = await fetch(`http://127.0.0.1:8000/task/detail/${params.taskid}/`, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        'Authorization': `Bearer ${data.access}`,
    })
    const taskData = await taskResponse.json()

    return taskData




}