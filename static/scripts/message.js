// Timeout Chip: handles multiple Flask flash messages.
setTimeout(()=> {
    let chip_message = document.getElementsByClassName("chip");

    for (let i = 0; i < chip_message.length; i++) {
        chip_message[i].style.display="none";
    }
}, 5000);