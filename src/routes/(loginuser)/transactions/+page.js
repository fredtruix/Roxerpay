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

    // transactionRes = await fetch()



}