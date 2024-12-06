<template>
    <nav class="bg-white border-gray-200 dark:bg-gray-900 p-1">
        <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
            <a href="" class="flex items-center space-x-3 rtl:space-x-reverse">
                <img src="../assets/images/shopping-cart.svg" class="h-8" alt="" />
                <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Shopcart</span>
            </a>
            <div class="flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse items-center">
                <button type="button"
                    class="flex items-center space-x-2 p-2 justify-center text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                    aria-label="Account">
                    <img src="../assets/images/account.svg" alt="Account Icon" class="w-6 h-6">
                    <span class="hidden md:inline text-gray-700 dark:text-gray-300 font-medium">Account</span>
                </button>
                <button type="button"
                    class="flex items-center space-x-2 p-2 justify-center text-sm text-gray-500 rounded-lg hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                    aria-label="Cart">
                    <img src="../assets/images/shopping-cart-bw.svg" alt="Cart Icon" class="w-6 h-6">
                    <span class="hidden md:inline text-gray-700 dark:text-gray-300 font-medium">Cart</span>
                </button>
                <button @click="toggleNavbar" type="button"
                    class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
                    aria-controls="navbar-cta" :aria-expanded="isNavbarVisible ? 'true' : 'false'">
                    <span class="sr-only">Open main menu</span>
                    <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                        viewBox="0 0 17 14">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 1h15M1 7h15M1 13h15" />
                    </svg>
                </button>
            </div>

            <div :class="{ 'block': isNavbarVisible, 'hidden': !isNavbarVisible }"
                class="items-center justify-between w-full md:flex md:w-auto md:order-1" id="navbar-cta">
                <ul
                    class="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:items-center md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">

                    <li>
                        <button @click="toggleCategories"
                            class="flex items-center justify-between w-full py-2 px-3 text-gray-900 rounded md:w-auto hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-blue-600 md:p-0 dark:text-white md:dark:hover:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:dark:hover:bg-transparent dark:border-gray-700">
                            Categories
                            <svg class="w-2.5 h-2.5 ms-2.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                                fill="none" viewBox="0 0 10 6">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                    stroke-width="2" d="m1 1 4 4 4-4" />
                            </svg>
                        </button>
                    </li>
                    <li>
                        <a href="#"
                            class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700"
                            aria-current="page">Deals</a>
                    </li>
                    <li>
                        <a href="#"
                            class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">What's
                            New</a>
                    </li>
                    <li>
                        <a href="#"
                            class="block py-2 px-3 md:p-0 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:hover:text-blue-700 md:dark:hover:text-blue-500 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent dark:border-gray-700">Delivery</a>
                    </li>
                    <li class="flex-grow md:flex md:items-center">
                        <form class="flex items-center space-x-2">
                            <label for="default-search" class="sr-only">Search</label>
                            <input type="search" id="default-search"
                                class="block w-full max-w-xs p-2 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                placeholder="Search..." required />
                            <button type="submit"
                                class="p-2 bg-white text-black rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-gray-600 dark:hover:bg-gray-700 dark:focus:ring-blue-800">
                                <svg class="w-5 h-5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                                    viewBox="0 0 20 20" stroke="black">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
                                </svg>
                            </button>
                        </form>
                    </li>
                </ul>
            </div>

        </div>
        <div v-if="isCategoriesVisible" id="mega-menu-full-dropdown"
            class="mt-1 border-gray-200 shadow-sm bg-gray-50 md:bg-white border-y dark:bg-gray-800 dark:border-gray-600">
            <div class="grid max-w-screen-xl px-4 py-5 mx-auto text-gray-900 dark:text-white sm:grid-cols-2 md:px-6">
                <ul>
                    <li>
                        <a href="#" class="block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700">
                            <div class="font-semibold">Online Stores</div>
                            <span class="text-sm text-gray-500 dark:text-gray-400">Connect with third-party tools
                                that you're already using.</span>
                        </a>
                    </li>
                    <li>
                        <a href="#" class="block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700">
                            <div class="font-semibold">Segmentation</div>
                            <span class="text-sm text-gray-500 dark:text-gray-400">Connect with third-party tools
                                that you're already using.</span>
                        </a>
                    </li>
                    <li>
                        <a href="#" class="block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700">
                            <div class="font-semibold">Marketing CRM</div>
                            <span class="text-sm text-gray-500 dark:text-gray-400">Connect with third-party tools
                                that you're already using.</span>
                        </a>
                    </li>
                </ul>
                <ul>
                    <li>
                        <a href="#" class="block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700">
                            <div class="font-semibold">Online Stores</div>
                            <span class="text-sm text-gray-500 dark:text-gray-400">Connect with third-party tools
                                that you're already using.</span>
                        </a>
                    </li>
                    <li>
                        <a href="#" class="block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700">
                            <div class="font-semibold">Segmentation</div>
                            <span class="text-sm text-gray-500 dark:text-gray-400">Connect with third-party tools
                                that you're already using.</span>
                        </a>
                    </li>
                    <li>
                        <a href="#" class="block p-3 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700">
                            <div class="font-semibold">Marketing CRM</div>
                            <span class="text-sm text-gray-500 dark:text-gray-400">Connect with third-party tools
                                that you're already using.</span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    data() {
        return {
            isNavbarVisible: false,
            isCategoriesVisible: false,
        };
    },
    methods: {
        toggleNavbar() {
            this.isNavbarVisible = !this.isNavbarVisible;
        },
        toggleCategories() {
            this.isCategoriesVisible = !this.isCategoriesVisible;
        }
    }
};
</script>
