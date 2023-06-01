import { fastWords, classicWords, bestWords } from '../data.js';

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
        classicPage = classicMaxPage;
    } else if (classicPage < 1) {
        classicPage = 1;
    }
    let classicPageData = paginateArray(classicWords, pageSize, classicPage);

    let bestPage = Number(url.searchParams.get('best_page') ?? '1');
    let bestMaxPage = Math.ceil(bestWords.length / pageSize)
    if (bestPage > bestMaxPage) {
        bestPage = bestMaxPage;
    } else if (bestPage < 1) {
        bestPage = 1;
    }
    let bestPageData = paginateArray(bestWords, pageSize, bestPage);

    return {
        fastPage: fastPage,
        fastMaxPage: fastMaxPage,
        fastTotal: fastWords.length,
        fastWords: fastPageData,

        classicPage: classicPage,
        classicMaxPage: classicMaxPage,
        classicTotal: classicWords.length,
        classicWords: classicPageData,

        bestPage: bestPage,
        bestMaxPage: bestMaxPage,
        bestTotal: bestWords.length,
        bestWords: bestPageData,

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
