<script lang="ts">
export default {
    data() {
        return {
            file: null as File | null,
            data: [{ name: "", href: "", open: false }]
        }
    },
    methods: {
        handleFileChange(event: any): void {
            this.file = event.target.files[0];
        },
        handleUpload(): void {
            if (!this.file) {
                console.log("Please select a file to upload.")
                return;
            }
            const reader = new FileReader();
            reader.onload = () => {
                let text = reader.result;
                if (typeof (text) !== null) {
                    this.data = JSON.parse(text as string)
                }

            }
            reader.readAsText(this.file);
        },
        toggleOpen(id: Number) {
            this.data.forEach((item, index) => {
                if (index === id) {
                    item.open = !item.open;
                } else {
                    item.open = false;
                }
            });
        }
    }
};
</script>

<template>
    <div class="main">
        <div class="uploadForm">
            <input type="file" ref="fileInput" @change="handleFileChange" />
            <button @click="handleUpload">Upload</button>
        </div>
        <div class="list-names">
            <ul>
                <li v-for="(item, index) in data" :key="index">
                    <div class="Name" @click="toggleOpen(index)">
                        {{ item.name }}
                    </div>
                    <transition class="Content" name="slide">
                        <div v-if="item.open" class="content">
                            <a v-bind:href="item.href" target="_blank">{{ item.href }}</a>
                        </div>
                    </transition>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.main {
    margin-top: 10rem;
}

.uploadForm {
    padding-left: 5vw;
}

.Name {
    font-size: 2vw;
}

.Name:hover {
    background-color: rgba(84, 84, 84, 0.65);
    transition: 0.4s;
}

.list-names {
    padding-left: 1vw;
    text-align: left;
}

.slide-enter-active,
.slide-leave-active {
    transition: all 0.3s ease;
}

.slide-enter,
.slide-leave-to {
    transform: translateY(-100%);
}
</style>
