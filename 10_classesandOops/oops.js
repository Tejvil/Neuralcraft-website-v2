const user = {
    username: "John",
    loginCount: 8,
    signedIn: true,

    getUserDetails: function(){
        console.log("Got user details");
    }

    

}
console.log(user.username);
console.log(user.getUserDetails());
