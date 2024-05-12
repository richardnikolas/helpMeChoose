<script>
    import { createEventDispatcher } from "svelte";

    let userPrompt;

    const dispatch = createEventDispatcher();
</script>

<style>
    #userInput {
        width: 100%;
        display: flex;
        align-items: center;
    }

    input[type=text] {
        height: 50px;
        border-radius: 10px;
        width: 80%;
        padding: 15px;
        font-size: 18px;
        margin: 0px 10px;
    }

    input[type=text]:focus {
        outline: none !important;
        border: 2px solid #df0d45;
    }

    .sendPromptBtn {
        width: 13%;
        height: 48px;
        border-radius: 10px;
        font-size: 22px;
        background-color: #df0d45;
        color: #FFF;
        cursor: pointer;
        margin: 0;
    }

    .sendPromptBtn:hover {
        background-color: #ad0c37;    
    }
</style>

<section id="userInput">
    <input type="text" bind:value={userPrompt} placeholder="Digite seu prompt aqui" />
    <button class="sendPromptBtn" on:click={() => dispatch("newUserPrompt", userPrompt)}>
        Enviar
    </button>
</section>