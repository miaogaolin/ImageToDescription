<script>
    export let data;
</script>

<div class="px-4 dark:bg-gray-900 text-gray-500 dark:text-gray-400">
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
        <div>
            <h1 class="text-center m-2 text-lg">Fast</h1>
            <div class="relative overflow-x-auto">
                <table class="w-full text-sm text-left">
                    <thead
                        class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
                    >
                        <tr>
                            <th scope="col" class="px-6 py-3"> 提示语 </th>
                            <th scope="col" class="px-6 py-3"> 数量 </th>
                            <th scope="col" class="px-6 py-3"> 词频 </th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each data.fastWords as item}
                            <tr
                                class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                            >
                                <th
                                    scope="row"
                                    class="px-6 py-4 font-medium text-gray-900 dark:text-white"
                                >
                                    {item[0]}
                                </th>
                                <td class="px-6 py-4"> {item[1]} </td>
                                <td class="px-6 py-4">
                                    {(Number(item[2]) * 100).toFixed(2)}%
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>

            <div class="flex flex-col items-center">
                <!-- Help text -->
                <span class="text-sm text-gray-900 dark:text-gray-400">
                    Showing <span
                        class="font-semibold text-gray-900 dark:text-white"
                        >{(data.fastPage - 1) * data.size + 1}</span
                    >
                    to
                    <span class="font-semibold text-gray-900 dark:text-white"
                        >{data.fastPage * data.size}</span
                    >
                    of
                    <span class="font-semibold text-gray-900 dark:text-white"
                        >{data.fastTotal}</span
                    >
                    Results
                </span>
                <div class="inline-flex mt-2 xs:mt-0">
                    <!-- Buttons -->
                    <button
                        class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-gray-800 rounded-l hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                        on:click={() => {
                            if (data.fastPage <= 1) {
                                return;
                            }
                            window.location.href =
                                "/words?fast_page=" +
                                (data.fastPage - 1) +
                                "&classic_page=" +
                                data.classicPage;
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
                            if (data.fastPage >= data.fastMaxPage) {
                                return;
                            }
                            window.location.href =
                                "/words?fast_page=" +
                                (data.fastPage + 1) +
                                "&classic_page=" +
                                data.classicPage;
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
        <div>
            <h1 class="text-center m-2 text-lg">Classic</h1>
            <div class="relative overflow-x-auto">
                <table class="w-full text-sm text-left">
                    <thead
                        class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
                    >
                        <tr>
                            <th scope="col" class="px-6 py-3"> 提示语 </th>
                            <th scope="col" class="px-6 py-3"> 数量 </th>
                            <th scope="col" class="px-6 py-3"> 词频 </th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each data.classicWords as item}
                            <tr
                                class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                            >
                                <th
                                    scope="row"
                                    class="px-6 py-4 font-medium text-gray-900 dark:text-white"
                                >
                                    {item[0]}
                                </th>
                                <td class="px-6 py-4"> {item[1]} </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    {(Number(item[2]) * 100).toFixed(2)}%
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
            <div class="flex flex-col items-center">
                <!-- Help text -->
                <span class="text-sm text-gray-900 dark:text-gray-400">
                    Showing <span
                        class="font-semibold text-gray-900 dark:text-white"
                        >{(data.classicPage - 1) * data.size + 1}</span
                    >
                    to
                    <span class="font-semibold text-gray-900 dark:text-white"
                        >{data.classicPage * data.size}</span
                    >
                    of
                    <span class="font-semibold text-gray-900 dark:text-white"
                        >{data.classicTotal}</span
                    >
                    Results
                </span>
                <div class="inline-flex mt-2 xs:mt-0">
                    <!-- Buttons -->
                    <button
                        class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-gray-800 rounded-l hover:bg-gray-900 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white"
                        on:click={() => {
                            if (data.classicPage <= 1) {
                                return;
                            }
                            window.location.href =
                                "/words?classic_page=" +
                                (data.classicPage - 1) +
                                "&fast_page=" +
                                data.classicPage;
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
                            if (data.classicPage >= data.classicMaxPage) {
                                return;
                            }
                            window.location.href =
                                "/words?classic_page=" +
                                (data.classicPage + 1) +
                                "&fast_page=" +
                                data.classicPage;
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
    </div>
</div>
