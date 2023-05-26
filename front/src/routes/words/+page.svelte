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
                            <th scope="col" class="px-6 py-3"> 序号 </th>
                            <th scope="col" class="px-6 py-3"> 单词 </th>
                            <th scope="col" class="px-6 py-3"> 数量 </th>
                            <th scope="col" class="px-6 py-3"> 词频 </th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each data.fastWords as item, index}
                            <tr
                                class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                            >
                                <td class="px-6 py-4">{index + 1}</td>
                                <th
                                    scope="row"
                                    class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                                >
                                    {item[0]}
                                </th>
                                <td class="px-6 py-4"> {item[1]} </td>
                                <td class="px-6 py-4">
                                    {(Number(item[2]) * 100).toFixed(2)} %
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
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
                            <th scope="col" class="px-6 py-3"> 序号 </th>
                            <th scope="col" class="px-6 py-3"> 单词 </th>
                            <th scope="col" class="px-6 py-3"> 数量 </th>
                            <th scope="col" class="px-6 py-3"> 词频 </th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each data.classicWords as item, index}
                            <tr
                                class="bg-white border-b dark:bg-gray-800 dark:border-gray-700"
                            >
                                <td class="px-6 py-4">{index + 1}</td>
                                <th
                                    scope="row"
                                    class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                                >
                                    {item[0]}
                                </th>
                                <td class="px-6 py-4"> {item[1]} </td>
                                <td class="px-6 py-4">
                                    {(Number(item[2]) * 100).toFixed(2)} %
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
