const botoes = document.querySelectorAll(".celula")
const erroDiv = document.querySelector('.pop');
const reiniciar = document.querySelector('.btn_reiniciar')
const avisos = document.querySelector('.espaco_avisos')
let m = false
avisos.innerText = "X  é  a  sua vez!"

for (let botao of botoes) {
    botao.addEventListener("click", function () {
        if(m === false){
            avisos.innerText = "O  é  a  sua vez!"
            m = true
        }else{
            avisos.innerText = "X  é  a  sua vez!"
            m = false 
        }

        let index = parseInt(botao.dataset.index)
        console.log(index)
        fetch(
            "/jogada", //rota
            {
                method: "POST", //metodo
                headers: { "Content-Type": "application/json" }, //tipo de dado (header)
                body: JSON.stringify({ "index": index }) //contetúdo que está sendo mandado
            }
        )

            .then(resposta => resposta.json())
            .then(dados => {
                if (dados.valida === true) {
                    botao.innerText = dados.simbolo
                }
                if (dados.resultado) {
                    erroDiv.innerText = 'Fim de jogo! ' + dados.resultado
                    erroDiv.classList.add('ativo');
                    setTimeout(() => {
                        for (let botao of botoes) {
                            botao.innerText = " "
                        }
                        erroDiv.classList.remove('ativo');
                        fetch(
                            "/reset", //rota
                            {
                                method: "POST" //metodo
                            }
                        )
                        m = false
                        avisos.innerText = "X  é  a  sua vez!"
                    }, 3000);

                }
            })

    })
}

reiniciar.addEventListener("click", function () {
    for (let botao of botoes) {
        botao.innerText = " "
    }
    m = false
    avisos.innerText = "X  é  a  sua vez!"
    fetch(
        "/reset", //rota
        {
            method: "POST" //metodo
        }
    )
})