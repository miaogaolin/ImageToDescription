import { fastWords, classicWords } from '../data.js';

export function load({ url }) {

    let pageSize = 100;
    let fastPage = Number(url.searchParams.get('fast_page') ?? '1');
    let fastMaxPage = Math.ceil(fastWords.length / pageSize)
    if (fastPage > fastMaxPage) {
        fastPage = fastMaxPage;
    } else if (fastPage < 1) {
        fastPage = 1;
    }
    let fastPageData = paginateArray(fastWords, pageSize, fastPage);


    let classicPage = Number(url.searchParams.get('classic_page') ?? '1');
    let classicMaxPage = Math.ceil(classicWords.length / pageSize)
    if (classicPage > classicMaxPage) {
        classicPage = fastMaxPage;
    } else if (classicPage < 1) {
        classicPage = 1;
    }

    let classicPageData = paginateArray(classicWords, pageSize, classicPage);
    return {
        fastPage: fastPage,
        fastMaxPage: fastMaxPage,
        fastTotal: fastWords.length,
        fastWords: fastPageData,

        classicPage: classicPage,
        classicMaxPage: classicMaxPage,
        classicTotal: classicWords.length,
        classicWords: classicPageData,

        size: pageSize,
    }
}

/**
 * @param {any[]} data
 * @param {number} page_size
 * @param {number} page_number
 */
function paginateArray(data, page_size, page_number) {
    return data.slice((page_number - 1) * page_size,
        page_number * page_size);
}
