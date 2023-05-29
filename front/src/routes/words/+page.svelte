<script>
    import Table from "./table.svelte";
    export let data;

    /**
     * @param {number} fastPage
     * @param {number} classicPage
     */
    function navigationUrl(fastPage, classicPage) {
        let url =
            "/words?fast_page=" + fastPage + "&classic_page=" + classicPage;

        return url;
    }
</script>

<div class="px-4 dark:bg-gray-900 text-gray-500 dark:text-gray-400">
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
        <Table
            data={data.fastWords}
            name="Fast"
            page={data.fastPage}
            size={data.size}
            total={data.fastTotal}
            prev_url={navigationUrl(data.fastPage - 1, data.classicPage)}
            next_url={navigationUrl(data.fastPage + 1, data.classicPage)}
            maxPage={data.fastMaxPage}
        />

        <Table
            data={data.classicWords}
            name="Classic"
            page={data.classicPage}
            size={data.size}
            total={data.classicTotal}
            prev_url={navigationUrl(data.fastPage, data.classicPage - 1)}
            next_url={navigationUrl(data.fastPage, data.classicPage + 1)}
            maxPage={data.classicMaxPage}
        />
    </div>
</div>
