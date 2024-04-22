// @ts-nocheck
import AuthStore from "../../../../stores/auth";



let data = "";


AuthStore.subscribe((data) => {
    data = data;
})



export const load = async ({fetch, params}) =>{
    console.log(params.id)

    let transactionResponse = await fetch(`http://127.0.0.1:8000/task/transaction/${params.id}/`,{
        method : "GET",
        headers : {"Content-Type": "application/json"},
        "Authorization":`Bearer ${data.access}`,
    })

    const transactionData = await transactionResponse.json()
    console.log(transactionData.data
        )
    return transactionData.data
}