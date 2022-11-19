import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import AppFooter from '@/components/AppFooter.vue'
import { computed } from 'vue'

describe('AppFooter.vue', () => {
  it('renders props.msg when passed', () => {
    const year = computed(() => new Date().getFullYear())
    const msg = 'Copyright © ' + year.value
    const wrapper = shallowMount(AppFooter)
    expect(wrapper.text()).to.include(msg)
  })
})
