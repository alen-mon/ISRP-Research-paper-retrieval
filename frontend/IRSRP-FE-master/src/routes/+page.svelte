<!-- +page.svelte -->
<script lang="ts">
    import SearchBar from "./SearchBar.svelte";
    import Loading from "./Loading.svelte";

    let fetching: boolean = false;

    let query: string = "";
    let papers: Paper[] = [];

    async function searchPapers() {
        fetching = true;
        console.log(query);
        const endpoint: string = `http://localhost:8000/search/?query=${query}`;
        
        const res = await fetch(endpoint, { method: "GET" });
        const data = await res.json();

        // Extract papers from the new JSON format
        papers = data.results.map((result: any) => ({
            title: result.title,
            authors: result.publisher, // Assuming publisher represents authors
            published: "", // You may need to extract this from the response
            category: result.subjects.join(", "), // Join subjects array into a string
            pdf_url: result.identifiers.find((id: string) => id.startsWith("url:"))?.substring(4), // Extract PDF URL from identifiers
            issn: result.identifiers.find((id: string) => id.startsWith("issn:"))?.substring(5) // Extract ISSN from identifiers
        }));

        fetching = false;
    }

    interface Paper {
        title: string;
        authors: string;
        published: string;
        category: string;
        pdf_url: string;
        issn: string;
    }
</script>

<style>
    /* Style for buttons */
    .search-button {
        display: inline-block;
        padding: 8px 16px;
        margin-right: 8px;
        border: 1px solid #007bff;
        border-radius: 4px;
        color: #007bff;
        background-color: transparent;
        text-decoration: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .search-button:hover {
        background-color: #007bff;
        color: #fff;
    }
</style>

<div data-sveltekit-preload-data="off" class="flex justify-center items-center">
    <div class="text-center">
        <p class="text-4xl mb-10 mt-10">Research Paper Retrieval System</p>
        <div class="mb-10">
            <SearchBar action={searchPapers} bind:value={query}/>
        </div>
        {#if !fetching}
            {#each papers as paper}
                <a target="_blank" href={paper.pdf_url} class="mb-4 block p-4 bg-white border border-gray-200 rounded-lg 
                shadow hover:bg-gray-100 dark:bg-gray-800 
                dark:border-gray-700 dark:hover:bg-gray-700">
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{paper.title}</h5>
                    <p class="font-normal">{paper.authors}</p>
                    <p class="font-normal text-gray-700 dark:text-gray-400">{paper.published}</p>
                    <div class="bg-slate-900">
                        <p class="font-normal">{paper.category}</p>   
                    </div>
                    <!-- Add a button for ISSN Link -->
                    <!-- Add Font Awesome icons to buttons -->
{#if paper.issn}
<button class="search-button" on:click={() => window.open(`${paper.pdf_url}`, "_blank")}>
    <i class="fas fa-file-pdf"></i> DOAJ
</button>
<button class="search-button" on:click={() => window.open(`https://portal.issn.org/resource/ISSN/${paper.issn}`, "_blank")}>
    <i class="fas fa-link"></i> ISSN Link
</button>
<!-- Add additional buttons for searching ISSN -->
<!-- You can find appropriate icons from Font Awesome and replace "fa-search" with appropriate icon class -->
<button class="search-button" on:click={() => window.open(`https://www.google.com/search?q=ISSN%20%22${paper.issn}%22`, "_blank")}>
    <i class="fas fa-search"></i> Google
</button>
<button class="search-button" on:click={() => window.open(`https://search.yahoo.com/search?p=ISSN%20%22${paper.issn}%22`, "_blank")}>
    <i class="fas fa-search"></i> Yahoo
</button>
<button class="search-button" on:click={() => window.open(`https://www.bing.com/search?q=ISSN%20%22${paper.issn}%22`, "_blank")}>
    <i class="fas fa-search"></i> Bing
</button>
<button class="search-button" on:click={() => window.open(`https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=ISSN%20%22${paper.issn}%22`, "_blank")}>
    <i class="fas fa-search"></i> IEEE
</button>
{/if}

                </a>
            {/each}
        {:else}
            <span class="text-center px-2 absolute -translate-y-1/2 -translate-x-1/2 top-2/4 left-1/2">
                <Loading/>
            </span>
        {/if}
    </div>
</div>
