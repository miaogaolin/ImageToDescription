<script>
    export let data;
</script>

<div class="p-4 dark:bg-gray-900">
    <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-4">
        {#each data.data as { fast, classic, best, iamge_path }}
            <div>
                <img
                    class="h-auto max-w-full rounded-lg"
                    src="https://imgs.iwaty.com/uploads/public{iamge_path}?x-oss-process=image/resize,w_300/format,webp"
                    alt=""
                />
                <div class="text-sm dark:text-gray-300 py-2">
                    <p>
                        <span class="text-lg font-medium">Fast:</span>
                        {fast}
                    </p>
                    <p class="mt-1">
                        <span class="text-lg font-medium">Classic:</span>
                        {classic}
                    </p>
                    <p class="mt-1">
                        <span class="text-lg font-medium">Best:</span>
                        {best}
                    </p>
                </div>
            </div>
        {/each}
    </div>
    <div class="flex flex-col items-center">
        <!-- Help text -->
        <span class="text-sm text-gray-900 dark:text-gray-400">
            Showing <span class="font-semibold text-gray-900 dark:text-white"
                >{(data.page - 1) * data.size + 1}</span
            >
            to
            <span class="font-semibold text-gray-900 dark:text-white"
                >{data.page * data.size}</span
            >
            of
            <span class="font-semibold text-gray-900 dark:text-white"
                >{data.total}</span
            >
            Images
        </span>
        <div class="inline-flex mt-2 xs:mt-0">
            <!-- Buttons -->
            <button
                class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-gray-800 rounded-l hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                on:click={() => {
                    if (data.page <= 1) {
                        return;
                    }
                    window.location.href = "/?page=" + (data.page - 1);
                }}
            >
                <svg
                    aria-hidden="true"
                    class="w-5 h-5 mr-2"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                    ><path
                        fill-rule="evenodd"
                        d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z"
                        clip-rule="evenodd"
                    /></svg
                >
                Prev
            </button>
            <button
                class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-gray-800 border-0 border-l border-gray-700 rounded-r hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                on:click={() => {
                    if (data.page >= data.maxPage) {
                        return;
                    }
                    window.location.href = "/?page=" + (data.page + 1);
                }}
            >
                Next
                <svg
                    aria-hidden="true"
                    class="w-5 h-5 ml-2"
                    fill="currentColor"
                    viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg"
                    ><path
                        fill-rule="evenodd"
                        d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                        clip-rule="evenodd"
                    /></svg
                >
            </button>
        </div>
    </div>
</div>
