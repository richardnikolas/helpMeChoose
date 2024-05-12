<script>
	const serverBaseUrl = "http://localhost:8000";

	import UserInput from "./components/UserInput.svelte";
	import MovieList from "./components/MovieList.svelte";

	let movieListResult = [];
	let isLoading;
	let hasError;

	async function getMoviesResponse(event) {
		let prompt = event.detail;

		hasError = false;
		isLoading = true;
		
		let fullUrl = serverBaseUrl + "/get-movies" + "?prompt=" + prompt;

		try {
			let response = await fetch(fullUrl);
			movieListResult = await response.json();
		} catch {
			hasError = true;
			console.error("Error while trying to reach API.");
		} finally {
			isLoading = false;
		}
	}
</script>

<style>
	#mainSection {
		background-color: #ede0e3;
		padding: 15px;
		display: flex;
		justify-content: center;
		align-items: center;
		width: 70%;
		height: auto;
		max-height: 90vh;
	}

	.content {
		width: 85%;
		text-align: center;
	}

	h1 {
		font-family: "Alfa Slab One";
		color: #df0d45;
		font-weight: 400;
		font-size: 66px;
		margin: 20px 0;
	}
</style>

<section id="mainSection">
	<div class="content">
		<h1>Help Me Choose!</h1>

		<p>Com a ajuda to <b>Google Gemini</b>, a ideia desse projeto é ajudar você a escolher qual o próximo <b>filme</b> que você irá assistir!</p>
		<p>Procure algo sobre sua atriz favorita, como por exemplo: "Quais foram os últimos filmes da Anne Hathaway?"</p>
		<p style="font-size: 11px">O foco desse projeto são apenas filmes, então séries e animes provavelmente não terão poster.</p>

		<UserInput on:newUserPrompt={getMoviesResponse} />

		<MovieList movieList={movieListResult} isLoading={isLoading} hasError={hasError} />
	</div>	
</section>
