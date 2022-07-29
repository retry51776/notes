# Volume
> secrets & configMap acts as volume too.

> Act as bridge between sidecars

## Volume Type
> There are so many Volumes, always go by official documentation
> https://kubernetes.io/docs/concepts/storage/volumes/
> https://kubernetes.io/docs/concepts/storage/persistent-volumes/

> Dynamic Storage Provisioning
> https://kubernetes.io/docs/concepts/storage/storage-classes/

> Universal Naming Convention (UNC)
- emptyDir `deleted after POD dead`
- hostPath `exists after POD dead. on node?`
- cephfs
- nfs
- iscsi
- secret
  - secret data `must be base64`
  - stringData `is string`
- configMap
- persistentVolumeClaim(PVC)

> StorageClass is similar to StorageProfile


### Cloud volumes
- gcePersistentDisk
- awsElasticBlockStore
- azureDisk
- azureFile