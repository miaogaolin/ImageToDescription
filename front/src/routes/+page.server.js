import { images } from './data.js';

export function load({ url }) {
    let pageSize = 30;
    let page = Number(url.searchParams.get('page') ?? '1');
    let maxPage = Math.ceil(images.length / pageSize)
    if (page > maxPage) {
        page = maxPage;
    } else if (page < 1) {
        page = 1;
    }
    let pageData = paginateArray(images, pageSize, page);

    return {
        maxPage: maxPage,
        page: page,
        size: pageSize,
        total: images.length,
        data: pageData.map((row) => ({
            fast: row.fast,
            classic: row.classic,
            iamge_path: '/' + row.image.substring(0, 3) + '/' + row.image.substring(3, 6) + '/' + row.image.substring(6, 9) + '/' + row.image
        }))
    };
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
