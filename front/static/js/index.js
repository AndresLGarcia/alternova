let trass = []
async function listarjokes() {
    try {
        const response = await fetch(`../getjokes/${user.value}`);
        const data = await response.json()
        descripcion.innerHTML = data.value
        trass = data

    } catch (error) {
        console.log(error);
    }
}

async function cargainicial() {
    await listarjokes()

    btnList.addEventListener('click', () => {
        listarjokes();
    })

    btnAdd.addEventListener('click', async () => {
        try {
            const response = await fetch(`../addjoke/${trass.id}/${email.value}`)
            if (response.status === 200) {
                alert('Jokes add successfully')
            }
        } catch (error) {
            alert(error);
        }
    })

    btnmyjokes.addEventListener('click', async () => {

        try {
            const response = await fetch(`../my_jokes/${email.value}`)
        } catch (error) {
            alert(error);
        }
    })

}

window.addEventListener("load", async () => {
    await cargainicial()

})