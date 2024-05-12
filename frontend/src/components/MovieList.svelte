<script>
    import Carousel from "svelte-carousel";
    import LoadingCircle from "./LoadingCircle.svelte";

    let carousel; // for calling methods of the carousel instance
  
    const handleNextClick = () => {
        carousel.goToNext()
    }

    export let movieList;
    export let isLoading;
    export let hasError;
</script>

<style>
    #movieList {
        transition: height 200ms ease-in-out;
        display: flex;
        margin: 10px 60px;
        justify-content: center;
    }
  
    .movieCard {
        margin: 10px 60px;
    }
  
    h2,
    p {
        margin: 0;
    }
  
    h2 {
        font-size: 2.25rem;
        font-family: var(--font-title);
        color: var(--white);
        line-height: 1.1;
    }
  
    p {
        font-family: var(--font-text);
        font-size: 0.9rem;
        line-height: 1.5;
        color: var(--white);
    }
  
    .flow > * + * {
        margin-top: var(--flow-space, 1em);
    }

    .errorBox {
        background-color: #eb2d2d;
        border: 2px solid #940606;
        border-radius: 10px;
        padding: 25px;
        margin: 30px;
    }

    .errorBox p {
        font-size: 16px;
    }
</style>

<section id="movieList">
    {#if isLoading}        
        <LoadingCircle />
    {:else if hasError}
        <div class="errorBox">
            <p style="font-weight: 600;">Desculpe! Algo deu errado na busca do seu prompt 😭</p>
            <p>Favor tentar novamente ou tentar outro prompt.</p>
        </div>
    {:else}
        {#if movieList.length === 0}
            <span></span>
        {:else}
            <Carousel 
                bind:this={carousel}
                particlesToShow={3}
                particlesToScroll={1}
                pauseOnFocus={true}
                autoplay={true}
                autoplayDuration={4500}
            >
                {#each movieList as movie, index (index)}
                    <div class="movieCard">
                        
                        <article class="card">
                            <img
                                class="card__background"
                                src={movie.posterUrl != null ? movie.posterUrl : "/assets/nullPoster.png"}
                                alt={movie.title}
                            />
                    
                            <div class="card__content | flow">
                                <div class="card__content--container | flow">
                                    <h2 class="card__title">{movie.title}</h2>

                                    <p class="card__description">
                                        {movie.synopsis}
                                    </p>

                                    <p class="card__description" >
                                        Nota: {movie.rating} ⭐
                                    </p>

                                    <p class="card__description" style="margin-top: 5px">
                                        Diretor(a): {movie.director}
                                    </p>
                                </div>
                            </div>
                        </article>
                    </div>
                {/each}
            </Carousel>
        {/if}
    {/if}
</section>
