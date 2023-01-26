<script lang="ts">
export default {
    data() {
        return {
            open: 0 as number,
            openKeys: [] as string[],
            openIndex: [] as string[],
            file: null as File | null,
            data: [] as [{ openid: number }] | {},
            typeofjson: 1
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
                    let parsedJSON = JSON.parse(text as string)
                    if (this.typeofjson === 1) {
                        let id = 0;
                        this.data = parsedJSON.map((item: any) => {
                            return Object.assign({}, item, { openid: id++ })
                        })
                    } else if (this.typeofjson === 2) {
                        this.data = parsedJSON
                    }
                }

            }
            reader.readAsText(this.file);
        },
        toggleOpen(id: any, type = ""): void {
            if (this.typeofjson === 2) {
                if (this.open == id) {
                    this.open = -1
                } else {
                    this.open = id
                }
            } else if (this.typeofjson === 1) {
                console.log(id)
                const loopArray = (Array: string[], key: string) => {
                    let found = false
                    Array.forEach((item, index) => {
                        if (item == key) {
                            delete Array[index]
                            found = true
                            return
                        }
                    });
                    if (!found) Array.push(key)
                }

                let key = type + String(id)
                if (type === "index") {
                    loopArray(this.openIndex, key);
                }
                else if (type === "keys") {
                    loopArray(this.openKeys, key);
                }
            }
        },
        setTypeOfJSON(type: number): void {
            this.typeofjson = type
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
        <div class="TypeButtons">
            <button :class="{ active: typeofjson === 1 }" @click="setTypeOfJSON(1)">display as JSON in array</button>
            <button :class="{ active: typeofjson === 2 }" @click="setTypeOfJSON(2)">display as JSON</button>
        </div>
        <div class="list-names">
            <ul v-if="typeofjson === 1">
                <li v-for="(item, index) in data" :key="index">
                    <div class="Name" @click="toggleOpen(index, 'index')" :key="index">
                        {{ index }}
                    </div>
                    <div class="SecName" v-for="(value, key, index2) in item" :key="index2">
                        <div v-if="openIndex.includes('index' + String(index))"
                            @click="toggleOpen(String(item.openid) + String(index2), 'keys')">
                            {{ key }}
                        </div>
                        <transition name="slide">
                            <div v-if="openKeys.includes('keys' + String(item.openid) + String(index2))"
                                class="content">
                                {{ value }}
                            </div>
                        </transition>
                    </div>


                </li>
            </ul>
            <ul v-else-if="typeofjson === 2">
                <li v-for="(value, key, index) in data" :key="index">
                    <div class="Name" @click="toggleOpen(index)">
                        {{ key }}
                    </div>
                    <transition name="slide">
                        <div v-if="open === index" class="content">
                            {{ value }}
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

.SecName {
    font-size: 2vw;
    margin-left: 4vw;
}

.SecName:hover {
    background-color: rgba(84, 84, 84, 0.65);
    transition: 0.4s;
}

.content {
    margin-left: 4vw;
}

.Name {
    font-size: 2vw;
}

.Name:hover {
    background-color: rgba(84, 84, 84, 0.65);
    transition: 0.4s;
}

.active {
    background-color: rgb(0, 55, 37);
}

.TypeButtons {
    margin-top: 2rem;
    margin-bottom: 2rem;
    padding-left: 5vw;
}

button,
input {
    background-color: rgb(3, 119, 80);
    border-radius: 1rem;
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    /* Green */
    border: none;
    color: white;
    margin-right: 1rem;
    padding: 7.5px 16px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
}

button:hover {
    box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19);
    background-color: rgb(0, 55, 37);
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
