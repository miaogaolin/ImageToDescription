<script>
    import Table from "./table.svelte";
    export let data;

    /**
     * @param {number} fastPage
     * @param {number} classicPage
     * @param {number} bestPage
     */
    function navigationUrl(fastPage, classicPage, bestPage) {
        let url =
            "/words?fast_page=" +
            fastPage +
            "&classic_page=" +
            classicPage +
            "&best_page=" +
            bestPage;

        return url;
    }
</script>

<div class="px-4 dark:bg-gray-900 text-gray-500 dark:text-gray-400">
    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <Table
            data={data.fastWords}
            name="Fast"
            page={data.fastPage}
            size={data.size}
            total={data.fastTotal}
            prev_url={navigationUrl(
                data.fastPage - 1,
                data.classicPage,
                data.bestPage
            )}
            next_url={navigationUrl(
                data.fastPage + 1,
                data.classicPage,
                data.bestPage
            )}
            maxPage={data.fastMaxPage}
        />

        <Table
            data={data.classicWords}
            name="Classic"
            page={data.classicPage}
            size={data.size}
            total={data.classicTotal}
            prev_url={navigationUrl(
                data.fastPage,
                data.classicPage - 1,
                data.bestPage
            )}
            next_url={navigationUrl(
                data.fastPage,
                data.classicPage + 1,
                data.bestPage
            )}
            maxPage={data.classicMaxPage}
        />

        <Table
            data={data.bestWords}
            name="Best"
            page={data.bestPage}
            size={data.size}
            total={data.bestTotal}
            prev_url={navigationUrl(
                data.fastPage,
                data.classicPage,
                data.bestPage - 1
            )}
            next_url={navigationUrl(
                data.fastPage,
                data.classicPage,
                data.bestPage + 1
            )}
            maxPage={data.bestMaxPage}
        />
    </div>
</div>
