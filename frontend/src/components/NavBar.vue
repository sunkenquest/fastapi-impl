<template>
    <div class="flex">
        <div class="flex">
            <div class="flex items-center space-x-2 px-10 py-10">
                <div class="w-6 h-6">
                    <img class="object-contain w-full h-full" src="../assets/images/shopping-cart.svg"
                        alt="Shopping cart">
                </div>
                <span class="text-lime-950">Shopcart</span>
            </div>
            <div class="flex items-center relative text-left py-10">
                <div>
                    <button @click="toggleDropdown"
                        class="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none">
                        <span class="text-lime-950">Categories</span>
                        <svg class="-mr-1 ml-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"
                            fill="currentColor">
                            <path fill-rule="evenodd"
                                d="M5.293 9.293a1 1 0 011.414 0L10 12.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                                clip-rule="evenodd" />
                        </svg>
                    </button>
                </div>

                <div v-if="isOpen"
                    class="absolute top-20 left-0 z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                    <div class="py-1" role="menu" aria-orientation="vertical" aria-labelledby="options-menu">
                        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">
                            Option 1
                        </a>
                        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">
                            Option 2
                        </a>
                        <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">
                            Option 3
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <div class="flex space-x-1">
            <div class="flex items-center py-4 px-4">
                <span class="text-sm">Deals</span>
            </div>
            <div class="flex items-center py-4 px-4">
                <span class="text-sm">What's new</span>
            </div>
            <div class="flex items-center py-4 px-4">
                <span class="text-sm">Deliveries</span>
            </div>
        </div>

        <div class="flex items-center w-full max-w-sm min-w-[200px] py-11 px-10">
            <div class="absolute">
                <input
                    class="w-full bg-transparent placeholder:text-slate-400 text-slate-700 text-sm border border-slate-200 rounded-md pl-3 pr-28 py-2 transition duration-300 ease focus:outline-none focus:border-slate-400 hover:border-slate-300 shadow-sm focus:shadow"
                    placeholder="Search Product" />
                <button
                    class="absolute top-1 right-1 flex items-center rounded bg-slate-800 py-1 px-2.5 border border-transparent text-center text-sm text-white transition-all shadow-sm hover:shadow focus:bg-slate-700 focus:shadow-none active:bg-slate-700 hover:bg-slate-700 active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
                    type="button">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"
                        class="w-4 h-4 mr-2">
                        <path fill-rule="evenodd"
                            d="M10.5 3.75a6.75 6.75 0 1 0 0 13.5 6.75 6.75 0 0 0 0-13.5ZM2.25 10.5a8.25 8.25 0 1 1 14.59 5.28l4.69 4.69a.75.75 0 1 1-1.06 1.06l-4.69-4.69A8.25 8.25 0 0 1 2.25 10.5Z"
                            clip-rule="evenodd" />
                    </svg>

                    Search
                </button>
            </div>
        </div>

        <div class="flex ml-10">
            <div class="flex items-center space-x-2 px-10 py-10">
                <div class="w-6 h-6">
                    <img class="object-contain w-full h-full" src="../assets/images/account.svg" alt="Shopping cart">
                </div>
                <span class="text-sm">Account</span>
            </div>
            <div class="flex items-center space-x-2 px-10 py-10">
                <div class="w-6 h-6">
                    <img class="object-contain w-full h-full" src="../assets/images/shopping-cart-bw.svg"
                        alt="Shopping cart">
                </div>
                <span class="text-sm">Cart</span>
            </div>
        </div>


    </div>
</ template>
<script>
export default {
    data() {
        return {
            isOpen: false,
        };
    },
    methods: {
        toggleDropdown() {
            this.isOpen = !this.isOpen;
        },
    },
};
</script>
